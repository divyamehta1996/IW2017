from django import forms
import datetime
from home.models import Facebook, Users
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class Signup(forms.ModelForm):
	hometown = forms.CharField(label='Location', max_length=100, required=False)
	books = forms.CharField(label='Favorite Book', max_length=100, required=False)
	music = forms.CharField(label='Favorite Music', max_length=100, required=False)
	sports = forms.CharField(label='Favorite Sport Team', max_length=100, required=False)
	checkins = forms.CharField(label='Favorite Restaurant', max_length=100, required=False)


	class Meta:
		model = Facebook
		fields = ['sports', 'music', 'books', 'checkins', 'hometown']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email')

class LoginForm(AuthenticationForm):
	username=forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

