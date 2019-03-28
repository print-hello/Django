from django import forms
from django.contrib.admin import widgets


class ChoiceDateForm(forms.Form):
    begintime = forms.DateField(required=True, label='时间', widget=widgets.AdminDateWidget())

