from django import forms
from .models import Plumbing

class ProblemForm(forms.ModelForm):

	class Meta:
		model = Plumbing
		fields = ('location', 'descr',)