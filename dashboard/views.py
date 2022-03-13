from django.shortcuts import render , redirect
from . forms import  LoginForm
# from django.contrib.auth import get_user_model,views as auth_views,update_session_auth_hash
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from . forms import  LoginForm
import datetime
from django.utils import timezone

#model imports
from products.models import products_table
from inventory.models import raw_material,finished_products
from .models import notifications
from finance.models import expenses,loader_expenses
#===============================index login===========================================#
def loginpage(request):
	user= request.user
	error = ''
	if not user.is_authenticated:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			try:
				user = authenticate(username = username , password = password)
				login (request,user)
				return redirect('home_page')
			except:
				error = 'Invalid username or password'
		context = {
			'error':error,
		}
		return render (request,'dashboard/login.html',context)
	else:
		return	redirect('home_page')
#####################################################choose page#########################################
@login_required (login_url='default_login')
def home_page(request):
	user = request.user
	####################### date data ##########################
	date = datetime.datetime.today()
	week = date.strftime("%U")
	year, week, _ = timezone.now().isocalendar()
	######################queries###############################
	products = finished_products.objects.all()
	raw_materials = raw_material.objects.all()
	my_notifications = notifications.objects.filter(user = None)|notifications.objects.filter(user = user)
	all_expenses = expenses.objects.filter(date__iso_year=year, date__week=week)
	all_loader_expenses = loader_expenses.objects.filter(date__iso_year=year, date__week=week)
	############################notifications####################
	count = 0 
	for notification in my_notifications:
		if notification.seen  is False:
			count +=1
		else:
			pass
	############################end notifications################

	context = {
		'user':user,
		'products':products,
		'raw_materials':raw_materials,
		'my_notifications':my_notifications,
		'count':count,
		'all_expenses':all_expenses,
		'all_loader_expenses':all_loader_expenses,
	}
	return render (request,'dashboard/index.html',context)
#################################################### logout##############################################
def logoutpage(request):
	logout(request)
	return redirect('default_login')