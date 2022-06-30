from django.urls import path,re_path
from . import views

urlpatterns = [
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('sign-up/',views.create_user, name='sign-up'),
   # path('search-events/', views.search_events, name='search-events'),
    # re_path(r'^events/(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.upcoming_events,name='show-events-for-this-month'),
    ]