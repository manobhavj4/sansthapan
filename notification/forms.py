from django import forms
from django.core.exceptions import ValidationError



class ContactForm(forms.Form):
	fullname= forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name"}))
	phone= forms.IntegerField(required=True,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your phone number"}))
	email= forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your email"}))
	content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Your content"}))

	def clean_email(self):
		email = self.cleaned_data.get("email")
		# if not "gmail.com" in email:
		# 	raise ValidationError("Email has to be gmail.com")
		return email 

	def clean_content(self):
		content = self.cleaned_data.get("content")
		if len(content) <=5:
			raise ValidationError("content must be more.. more than 5 letters")
