from django import forms

class LoginForms(forms.Form):
    username=forms.CharField(required=True)
    # username=forms.CharField( max_length=50, required=False)
    pwd = forms.CharField(min_length=4,max_length=20, required=False)