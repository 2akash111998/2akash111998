from django.conf.urls import url
from userLogin import views

app_name = 'userLogin'

urlpatterns = [
	# url(r"^$", views.index, name = 'index'),
	url(r'^$', views.index, name = 'index'),
	url(r'^form/', views.register, name = 'form'),
	url(r'^thanku/', views.thank_you, name = 'thank_you'),
	url(r'^logout/', views.user_logout, name = 'user_logout'),
	url(r'^login/', views.user_login, name = 'user_login'),
]