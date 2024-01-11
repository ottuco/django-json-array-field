from django import forms

from json_array_field.forms.fields import JSONArrayFormField
from tests.polls.models import JSONArrayFieldModel


class JSONArrayForm(forms.Form):
    list_field = JSONArrayFormField()


class JSONArrayModelForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = JSONArrayFieldModel
