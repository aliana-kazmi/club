from django import views
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import calendar
from calendar import Calendar, HTMLCalendar
from .models import Event, Venue
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
     return render(request, 'events/calender_base.html', {'title':title, 'cal':cal})
     #return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,cal)) this shows the basic version of cal which is non-editable

# Scheduled Events
def all_events(request):
    all_events_list = Event.objects.all()
    title = 'Scheduled Events'
    return render(request, 'events/event_list.html',{'title':title, 'events_list':all_events_list})

# upcoming events in this month
def upcoming_events(request, year, month):
    year = int(year)
    month = int(month)
    events_list = Event.objects.filter(
        event_date__year=year,
        event_date__month = month
        )
    month_name = calendar.month_name(month)
    title = f'Scheduled Events In {month_name}, {year}'
    return render(request, 'events/event_list.html',{'title':title, 'events_list':events_list})

def search_events(request):
    if request.method == "POST":
        
        searched=request.POST.get('searched')
        if searched:
            pass
        else:
            searched=" "
        event_list = Event.objects.filter(name__contains=searched)
        return render(request, 'events/search_events.html', {'searched':searched, 'event_list':event_list})
    else:
        return render(request, 'events/search_events.html',{})
    


def search_venues(request):
    if request.method == "POST":
        
        searched=request.POST.get('searched')
        if searched:
            pass
        else:
            searched=" "
        venue_list = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched':searched, 'venue_list':venue_list})
    else:
        return render(request, 'events/search_venues.html',{})
# local venues
def local_venues(request):
    venue_list = Venue.objects.filter(zip_code='226003')
    title = 'Local Venues'
    return render(request, 'events/venue_list.html',{'title':title, 'venue_list':venue_list})

def add_venue(request):
     submitted = False
     if request.method == 'POST':
         form = VenueForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/add-venue/?submitted=True')
     else:
         form = VenueForm()
         if 'submitted' in request.GET:
             submitted = True
     return render(request, 
         'events/add_venue.html', 
         {'form': form, 'submitted': submitted}
         )