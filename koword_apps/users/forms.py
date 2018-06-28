# -*- coding: utf-8 -*-
import json

from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=6, max_length=20)
	password = forms.CharField(required=True, min_length=6, max_length=200)