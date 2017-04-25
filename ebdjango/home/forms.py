from django import forms
import datetime
from home.models import Facebook, Users
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signup(forms.ModelForm):
	hometown = forms.CharField(label='Location', max_length=100)
	books = forms.CharField(label='Favorite Book', max_length=100)
	music = forms.CharField(label='Favorite Music', max_length=100)
	sports = forms.CharField(label='Favorite Sport Team', max_length=100)
	checkins = forms.CharField(label='Favorite Restaurant', max_length=100)


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

