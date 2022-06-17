from django import forms
from django.forms import ModelForm
from .models import Venue

class VenueForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Venue
        # we’re using the special __all__ value to tell Django to use all the form fields
        fields = '__all__'
        labels = {
			'name': 'Name     ',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email_address': '',
			'venue_image': '',			
		}
        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name', 'style':'margin:0.5rem'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address', 'style':'margin:0.5rem'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code', 'style':'margin:0.5rem'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone', 'style':'margin:0.5rem'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address', 'style':'margin:0.5rem'}),
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'style':'margin:0.5rem'}),
		}
    def clean(self):
         cleaned_data = super().clean()
         phone = cleaned_data.get("phone")
         email_address = cleaned_data.get("email_address")
         if not (phone or email_address):
             raise forms.ValidationError(
                 "You must enter either a phone number or an email, or both."
             )