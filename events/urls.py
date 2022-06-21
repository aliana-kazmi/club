from django.urls import path,re_path
from . import views

urlpatterns = [
    
    path('',views.index,name='default'),
    path('add-venue/', views.add_venue, name='add-venue'),
    path('local-venues/', views.local_venues, name='show-local-venues'),
    path('search-venues/', views.search_venues, name='search-venues'),
    path('all-events/', views.all_events, name='show-events'),
    path('search-events/', views.search_events, name='search-events'),
    re_path(r'^events/(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.upcoming_events,name='show-events-for-this-month'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.calender_base, name='calender'),#can process the right format
    ]