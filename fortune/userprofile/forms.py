import datetime

from django import forms
from django.contrib.auth.models import User

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

	def clean_username(self):
		# check if new username is same as old one (for update of instance)
		if self.cleaned_data['username'] == self.initial['username']:
			return self.cleaned_data['username']

		# check if username is used or not
		try:
			existing_user = User.objects.get(username=self.cleaned_data['username'])
			raise forms.ValidationError("Username is already used!")
		except User.DoesNotExist:
			pass
		return self.cleaned_data['username']

	def clean_birth_date(self):
		# check if birth_date is larger than today
		birth_dt = self.cleaned_data['birth_date']
		if birth_dt > datetime.date.today():
			raise forms.ValidationError("Birth date can't be great than today")
		return birth_dt
