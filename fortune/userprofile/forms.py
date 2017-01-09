from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile


class UserForm(forms.ModelForm):
	"""
	Customised user profile form
	"""
	username = forms.CharField()
	birth_date = forms.DateField()

	class Meta:
		model = UserProfile
		fields = ['username', 'birth_date']

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-4'
		self.helper.field_class = 'col-md-4'
		self.helper.add_input(Submit('submit', 'Submit'))
