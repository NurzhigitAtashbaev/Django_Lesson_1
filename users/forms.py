from django import forms


class AuthFrom(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)