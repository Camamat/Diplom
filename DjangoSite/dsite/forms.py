from django import forms

class UserRegisterForm(forms.Form):
    login_ = forms.CharField(max_length=20)
    password = forms.PasswordInput()
    age = forms.IntegerField(max_value=100)
