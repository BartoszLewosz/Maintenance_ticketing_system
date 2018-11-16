from django import forms
from .models import Maintenance

class MaintenanceForm(forms.ModelForm):

	class Meta:
		model = Maintenance
		fields = ('location', 'descr', 'status', 'priority',)
		widgets = {
		'descr': forms.Textarea(attrs={'rows':4, 'cols':25}),
		}