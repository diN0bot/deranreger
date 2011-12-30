from django import forms


__all__ = ["DataForm"]


class DataForm(forms.Form):
    name = forms.CharField(max_length=100)
