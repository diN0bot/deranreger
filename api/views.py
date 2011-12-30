from deranreger.api.views_base import BaseJSONView
from deranreger.api.forms import DataForm


__all__ = ["DataView"]


class DataView(BaseJSONView):
    form_class = DataForm
    #success_message = "Data added!"
