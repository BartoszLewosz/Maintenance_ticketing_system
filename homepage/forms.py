from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text=None)
	email = forms.EmailField(max_length=254, help_text='Required')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
	class Meta:
		model = User
		fields = ('username', 'first_name', 'email', 'password1', 'password2',)
