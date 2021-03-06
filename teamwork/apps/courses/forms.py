from django import forms

from .models import *

class CourseForm(forms.ModelForm):

	# used for filtering the queryset
	def __init__(self, uid, *args, **kwargs):
		super(CourseForm, self).__init__(*args, **kwargs)
		# exclude the current user and the superuser
		self.fields['students'].queryset = User.objects.exclude(id=uid).exclude(is_superuser=True)
    
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=255)
	students = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=User.objects.all())
	class Meta:
	    model = Course
	    fields = ['name']
