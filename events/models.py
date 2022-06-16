from django.db import models
from django.contrib.auth.models import User

# class VenueManager(models.Manager):
#   def get_queryset(self):
#     return super(VenueManager,self).filter(zip_code='226003')

class Venue(models.Model):
      name = models.CharField('Venue Name', max_length=120)
      address = models.CharField(max_length=300)
      zip_code = models.CharField('Zip/Post Code', max_length=12)
      phone = models.CharField('Contact Phone', max_length=20, blank=True)
      web = models.URLField('Web Address',blank=True)
      email_address = models.EmailField('Email Address',blank=True)

      # local_venues = VenueManager()

      def __str__(self):
        return self.name
 
 
class MyClubUser(models.Model):
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     email = models.EmailField('User Email')
 
     def __str__(self):
         return self.first_name + " " + self.last_name
 
 
# class EventManager(models.Manager):
#   def get_queryset(self,month):
#     response  = super(EventManager,self).filter(event_date__year=year, event_date__month=month)
#     return response
#     # return super(EventManager,self).filter(datetime_published__month=month)

class Event(models.Model):
     name = models.CharField('Event Name', max_length=120)
     event_date = models.DateTimeField('Event Date')
     venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
     manager = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True, max_length = 60)
     attendees = models.ManyToManyField(MyClubUser, blank=True)
     description = models.TextField(blank=True)

    #  specific_events = EventManager()
 
     def __str__(self):
         return self.name