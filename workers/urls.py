from django.urls import path ,re_path ,include
from . import views
from django.contrib.auth import views as auth_views


#these are the urls that redirect to the function that actually runs the application

urlpatterns = [
	path('weekly_employment_form/',views.weekly_employment_form,name = 'weekly_employment_form'),
	path('get_worker_pay_value/<int:id>/',views.get_worker_pay_value,name = 'get_worker_pay_value'),
]
