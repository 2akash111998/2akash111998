# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	my_dict = { 'insert_content': 'Hello im from userLogin/index.html' }
	return render(request, 'userLogin/index.html', context = my_dict)

	