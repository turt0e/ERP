from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    def clean_username(self):
        username = self.cleaned_data.get('username')
        foo = User.objects.filter(username=username)
        if foo.exists():
            raise forms.ValidationError('Username already exists.')
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        foo = User.objects.filter(email=email)
        if foo.exists():
            raise forms.ValidationError('This email is already taken.')
    def clean_password_confirm(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password_confirm != password:
            raise forms.ValidationError('Password does not match.')
        return data
