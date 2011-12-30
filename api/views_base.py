from django import http
from django.utils import simplejson as json
from django.views.generic.base import View
from django.views.generic.edit import FormMixin


__all__ = ["BaseJSONView"]


class JSONResponseMixin(object):
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
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)


class BaseJSONView(FormMixin, View, JSONResponseMixin):

    def form_valid(self, form, request):
        form.save()
        return self.api_response(self.success_message)

    def form_invalid(self, form):
        return self.api_response(form.errors, status=500)

    def api_response(self, data=None, status=None):
        return self.render_to_response(data)

    def get(self, request, *args, **kwargs):
        return self.api_response(data={'hello':'world'})

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)
