from django.conf.urls import url
from userLogin import views

app_name = 'userLogin'

urlpatterns = [
	# url(r"^$", views.index, name = 'index'),
	url(r'^$', views.index, name = 'index'),
	url(r'^form_name/', views.form_name_view, name = 'form_name_view'),
	url(r'^thanku/', views.thank_you, name = 'thank_you')
]