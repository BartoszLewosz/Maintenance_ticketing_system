from django import forms
from .models import Electric

class ElectricForm(forms.ModelForm):
	
	class Meta:
		model = Electric
		fields = ('location', 'descr',)

	