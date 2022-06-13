from django import views
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event
from .forms import VenueForm

def index(request):
    year=date.today().year
    month=date.today().month
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name,year)
    cal= HTMLCalendar().formatmonth(year,month)
    return render(request, 'events/calender_base.html', {'cal':cal})

def calender_base(request,year,month):
     year = int(year)
     month = int(month)
     title = ""
     if year < 2010 or year > 2500: 
         title= "Year out of bounds. Please choose another date."
         year=date.today().year
         month=date.today().month
     month_name = calendar.month_name[month]
     cal= HTMLCalendar().formatmonth(year,month)
     title += "Event Calendar - %s %s" % (month_name,year)
    #  events_list = Event.objects.all()
     return render(request, 'events/calender_base.html', {'title':title, 'cal':cal})
     #return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,cal)) this shows the basic version of cal which is non-editable

def all_events(request):
    events_list = Event.objects.all()
    return render(request, 'events/event_list.html',{'events_list':events_list})


def add_venue(request):
     submitted = False
     if request.method == 'POST':
         form = VenueForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/add_venue/?submitted=True')
     else:
         form = VenueForm()
         if 'submitted' in request.GET:
             submitted = True
     return render(request, 
         'events/add_venue.html', 
         {'form': form, 'submitted': submitted}
         )