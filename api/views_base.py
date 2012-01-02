from django import http
from django.utils import simplejson as json
from django.views.generic.base import View
from django.views.generic.edit import FormMixin
import pyes
from time import mktime
from django.conf import settings


__all__ = ["BaseJSONView"]


class JSONResponseMixin(object):
    structure_definitions = {'datetime': lambda dt: int(mktime(dt.timetuple())) }

    def render_to_response(self, adict):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(adict))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, adict):
        "Convert the context dictionary into a JSON object"
        self._smash(adict)
        return json.dumps(adict)

    def _smash(self, adict):
        for key, value in adict.iteritems():
            try:
                adict[key] = self.structure_definitions[value.__class__.__name__](value)
            except KeyError:
                pass


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
