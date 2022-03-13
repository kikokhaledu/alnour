from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout, authenticate



################################################Login###############################################
class LoginForm(forms.Form):
	email = forms.CharField(label= 'email')
	password = forms.CharField(label = 'password',widget = forms.PasswordInput)

	def clean(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		if email and password :
			user =authenticate(email = email , password = password )
			if not user:
				raise forms.ValidationError('the credintials you provided were incorrect please try again ')
			if not user.check_password(password):
				raise forms.ValidationError('password is incorrect please check your password and try again ')
			if not user.is_active:
				raise forms.ValidationError('please activate your account by clicking the email sent to you when you registred')
		return super(LoginForm,self).clean(*args,**kwargs)
