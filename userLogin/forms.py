from django import forms
from django.contrib.auth.models import User
from userLogin.models import user_obj


class user_form(forms.ModelForm):

	# name = forms.CharField()
	# email = forms.EmailField()

	passsword = forms.CharField(widget = forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'passsword')

class user_profile_info_form(forms.ModelForm):
	class Meta():

		# The model is user_obj 
		model = user_obj
		# Doubt at this step
		# My guess is that we want to only extract these two field from the form 
		fields = ('profile_pic', 'nick_name')
