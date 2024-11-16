from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django import forms

# Форма для регистрации
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

# class RegisterForm(UserCreationForm):
#     username = forms.CharField(
#         max_length=32,
#         required=True,
#         help_text="Enter your Telegram username (without @)."
#     )
#     email = forms.EmailField(required=True, help_text="Enter your email address.")
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if not username.isalnum() and "_" not in username:
#             raise forms.ValidationError("Telegram usernames can only contain letters, numbers, and underscores.")
#         if len(username) > 32:
#             raise forms.ValidationError("Telegram usernames cannot exceed 32 characters.")
#         return username