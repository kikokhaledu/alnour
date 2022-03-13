from django.shortcuts import render , redirect
from . forms import  LoginForm
# from django.contrib.auth import get_user_model,views as auth_views,update_session_auth_hash
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from . forms import  LoginForm
#model imports
from products.models import products_table
from inventory.models import raw_material,finished_products
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
	products = finished_products.objects.all()
	raw_materials = raw_material.objects.all()
	context = {
		'user':user,
		'products':products,
		'raw_materials':raw_materials,
	}
	return render (request,'dashboard/index.html',context)
#################################################### logout##############################################
def logoutpage(request):
	logout(request)
	return redirect('default_login')