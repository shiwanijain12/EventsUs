from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organizer(models.Model):
    name= models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)
    date_registered= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)
    date_registered= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    

class Event(models.Model):
    CATEGORY_CHOICES = (
        ('Concerts', 'Concerts'),
        ('Classes & Workshops', 'Classes & Workshops'),
        ('Corporate Events', 'Corporate Events'),
        ('Festivals & Fairs', 'Festivals & Fairs'),
    )

    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,null=True)
    start_date = models.DateTimeField(null= True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)
    
