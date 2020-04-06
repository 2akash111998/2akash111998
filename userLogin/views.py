# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required	

from userLogin.forms import user_form, user_profile_info_form
from userLogin.models import user_obj
from django.contrib.auth.models import User
# Create your views here.

def index(request):
	return render(request, 'userLogin/index.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('userLogin:index'))

def register(request):
	registered = False

	if request.method == 'POST'	:
		userForm = user_form(data = request.POST)
		userProfileInfoForm = user_profile_info_form(data = request.POST)

		if userForm.is_valid() and userProfileInfoForm.is_valid():
			user = userForm.save()
			user.set_password(user.password)

			user_profile = userProfileInfoForm.save(commit = False)
			user_profile.user = user

			if 'profile_pic' in request.FILES:
				user_profile.profile_pic = request.FILES['profile_pic']

			user_profile.save()
			# print('SAVED................................')
			registered = True

		else:
			print(userForm.errors, userProfileInfoForm.errors)
	else:
		userForm = user_form()
		userProfileInfoForm = user_profile_info_form()

	return render(request, 'userLogin/form.html', {'user_form':userForm, 'profile_form':userProfileInfoForm,
		'registered':registered})




def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('userLogin:index'))
			else:
				return HttpResponse('ACCCOUNT NOT ACTIVE')
		else:
			print('An attempt to login failed ..........')
			print('username: {}  password: {}'.format(username, password))
			return HttpResponse('Invalid login details supplied')
	else:
		return render(request, 'userLogin/login.html', {})

def thank_you(request):
	return render(request, 'userLogin/thanku.html',)