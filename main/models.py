from django.db import models
from django import forms
from captcha.fields import CaptchaField

# Create your models here.
class Account(models.Model): 
    username = models.CharField(max_length=200, primary_key=True, null=False)
    nickname = models.CharField(max_length=200, default='CAT')
    password = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.username

class LoginForm (forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    captcha = CaptchaField(label='機器人驗證...')

