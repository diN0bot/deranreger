from django import http
from django.utils import simplejson as json
from django.views.generic.base import View
from django.views.generic.edit import FormMixin
import pyes
from time import mktime
from django.conf import settings


__all__ = ["BaseJSONView"]


class JSONResponseMixin(object):

    def __init__(self):
        super(JSONResponseMixin, self).__init__()
        self.structure_definitions = {'dict': self._smash,
                                      'list': self._smash,
                                      'datetime': lambda dt: int(mktime(dt.timetuple())) }

    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        context = self._smash(context)
        return json.dumps(context)

    def _smashit(self, context):
        try:
            return self.structure_definitions[context.__class__.__name__](context)
        except KeyError:
            return context

    def _smash(self, context):
        if hasattr(context, 'iteritems'):
            return self._dict_smash(context)
        elif hasattr(context, 'append'):
            return self._list_smash(context)
        else:
            return self._smashit(context)

    def _dict_smash(self, adict):
        ret = {}
        for key, value in adict.iteritems():
            ret[key] = self._smashit(value)
        return ret

    def _list_smash(self, alist):
        newlist = []
        for value in alist:
            newlist.append(self._smashit(value))
        return newlist


class ElasticSearchMixin(object):

    def retrieve_data(self):
        conn = pyes.ES(settings.ELASTICSEARCH_CLUSTER[0])
        query = pyes.WildcardQuery("_all", "*")
        data = conn.search(query=query)
        ret = []
        for doc in data:
            newdoc = {}
            for key in doc:
                if key != 'meta':
                    newdoc[key] = doc[key]
            ret.append(newdoc)
        return ret


class BaseJSONView(FormMixin, View, JSONResponseMixin, ElasticSearchMixin):

    def __init__(self):
        JSONResponseMixin.__init__(self)

    def form_valid(self, form, request):
        #response = self._es_conn.index(form.document())
        return self.api_response(self.success_message)

    def form_invalid(self, form):
        return self.api_response(form.errors, status=500)

    def api_response(self, data=None, status=None):
        return self.render_to_response(data)

    def get(self, request, *args, **kwargs):
        data = self.retrieve_data()
        return self.api_response(data={'data': data})

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)
