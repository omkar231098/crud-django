from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    city = forms.CharField(max_length=100)

class UpdateForm(forms.Form):
    key = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)

class DeleteForm(forms.Form):
    key_to_delete = forms.CharField(max_length=100)
