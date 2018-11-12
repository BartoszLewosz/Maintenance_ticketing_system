from django import forms
from .models import Electric

class ElectricForm(forms.ModelForm):
	
	class Meta:
		model = Electric
		fields = ('location', 'descr','status',)
		widgets = {
		'descr': forms.Textarea(attrs={'rows':4, 'cols':25}),
		}


	