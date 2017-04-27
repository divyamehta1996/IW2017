from django import forms
import datetime
from home.models import Users, UserWishlist
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class Signup(forms.ModelForm):
	name = forms.CharField(label='Full Name', max_length=50)
	gender = forms.CharField(label='Gender', max_length=25, required=False)
	birthDate = forms.DateField(label='Birth Date', widget=SelectDateWidget(years=range(1985, datetime.date.today().year+10)))
	city = forms.CharField(label='Current city', max_length=100, required=False)
	state = forms.CharField(label='Current state', max_length=100, required=False)
	books = forms.CharField(label='Favorite Books', max_length=100, required=False)
	music = forms.CharField(label='Favorite Music', max_length=100, required=False)
	sports = forms.CharField(label='Favorite Sport Teams', max_length=100, required=False)
	checkins = forms.CharField(label='Favorite Restaurants or Places', max_length=100, required=False)

	class Meta:
		model = Users
		fields = ['name', 'gender', 'birthDate', 'city', 'state', 'books', 'music', 'sports', 'checkins']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email')

class Wishlist(forms.ModelForm):
	item = forms.CharField()

	class Meta:
		model = UserWishlist
		fields = ['item']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""


# class LoginForm(AuthenticationForm):
# 	username=forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
# 	password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
