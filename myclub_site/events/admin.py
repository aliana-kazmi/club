from django.contrib import admin
from .models import Event, Venue, MyClubUser
# Register your models o the website here.

# IN PLACE OF admin.site.register(Venue)(
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone')
    ordering = ('name',)
    search_fields = ('name','address','phone')


# admin.site.register(Event)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    #mention the fields to be displayed in fields and those who are to be displayed in same line are to be put into a tuple
    fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('name','event_date','venue','manager')
    ordering = ('event_date',)
    search_fields = ('name','event_date','venue','manager')


# admin.site.register(MyClubUser)
@admin.register(MyClubUser)
class MyClubUserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    ordering = ('first_name',)
    search_fields = ('first_name','last_name')