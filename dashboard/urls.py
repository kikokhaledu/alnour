from django.urls import path ,re_path ,include
from . import views
from django.contrib.auth import views as auth_views


#these are the urls that redirect to the function that actually runs the application

urlpatterns = [
	path('',views.loginpage,name = 'default_login'),#home
    path('home_page/',views.home_page, name= 'home_page'),
    path('logoutpage/', views.logoutpage , name = 'logoutpage'),    
    # path('PasswordChange/', views.PasswordChange , name = 'PasswordChange'),    
]
