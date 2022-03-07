from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailInput
from django.utils.translation import gettext_lazy as _


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=EmailInput)

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
