# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from forms import FormName
from userLogin.models import User
# Create your views here.

def index(request):
	my_dict = { 'insert_content': 'Hello im from userLogin/index.html' }
	return render(request, 'userLogin/index.html', context = my_dict)

def form_name_view(request):
	form = FormName(request.POST)
	# print('IM HERE')
	if form.is_valid():
		obj = User()
		obj.name = form.cleaned_data['name']
		obj.email = form.cleaned_data['email']
		obj.save()
		return HttpResponseRedirect('/')
			
	return render(request, 'userLogin/form_name.html', {'form':form})