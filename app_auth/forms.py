from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur",widget=forms.TextInput(attrs={'class':'input form-control ','placeholder':"Nom d'utilisateur"}),required=True)
    # username=forms.CharField( max_length=50, required=False)
    pwd = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':' input form-control','placeholder':'Mot de passe'}),min_length=4,max_length=20, required=True)

class SignupForm(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur",widget=forms.TextInput(attrs={'class':'input form-control ','placeholder':"Nom d'utilisateur"}),required=True)
    pwd = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':' input form-control','placeholder':'Mot de passe'}),min_length=4,max_length=20, required=True)
    comfirmPwd = forms.CharField(label="Mot de passe de confir",widget=forms.PasswordInput(attrs={'class':' input form-control','placeholder':'comfirmez mot de passe'}),min_length=4,max_length=20, required=True)