from urllib import request
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection


class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=40,label='User name')
    email = forms.EmailField(required=False, label='Your Email Address')
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
     submitted = False
     if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             # assert False
             con = get_connection('django.core.mail.backends.console.EmailBackend')
             send_mail(
                 cd['title'],
                 cd['message'],
                 cd.get('email', 'noreply@example.com'),
                 ['siteowner@example.com'],
                 connection=con
             )
             return HttpResponseRedirect('/contact?submitted=True')
     else:
         form = ContactForm()
         if 'submitted' in request.GET:
             submitted = True
 
     return render(request, 
         'contact.html', 
         {'form': form, 'submitted': submitted}
         )