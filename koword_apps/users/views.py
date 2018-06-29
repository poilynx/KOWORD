# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from .forms import LoginForm, RegisterForm
from .models import UserProfile



from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404


from django.shortcuts import render, redirect

from django.conf import settings

class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
		  user = UserProfile.objects.get(Q(username=username)|Q(email=username))
		  if user.check_password(password): 	# password stored in backend is encrypted
		      return user 					# success to login
		except Exception as e:
			 return None							# fail to login


class LoginView(View):
    def get(self, request):
        return render(request, "user_login.html", {})

    def post(self, request):
    	loginform = LoginForm(request.POST)	# test if input is valid
    	if loginform.is_valid():				# input is valid, then get login inpu 
    		username = request.POST.get("username", "")
    		password = request.POST.get("password", "")
    		user = authenticate(username=username, password=password)	
    		if user is not None:				# user is valid
    			login(request, user)	
    			return render(request, "user_login.html", {
                    "msg": "success to login!"
                })	# success to login
    		else:
    			return render(request, "user_login.html", {  # fail to login
                    'loginform': loginform,
                    "msg": "Username or password is wrong!"
                })	
    	else:
            return render(request, "user_login.html", { # input is not valid
                'loginform': loginform
            }) 


class RegisterView(View):
    def get(self, request):
        registerform = RegisterForm()
        return render(request, "user_register.html", {
            'registerform':registerform,
            'method': 'email'
        })

    def post(self, request):
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "user_register.html", {
                    "register_form":register_form,
                    "msg":"用户{0}已经存在".format(user_name),
                    "method": "email"
                })
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.nick_name = register_form.data["nickname"]
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email_async.delay(user_name, "register", request.get_host())
            return render(request, "user_login.html", {"login_title": u"注册成功，请检查你的邮箱中的确认邮件。账号激活之后就可以登录了。"})
        else:
            return render(request, "user_register.html", {
                "register_form": register_form,
                "method": "email"
            })

