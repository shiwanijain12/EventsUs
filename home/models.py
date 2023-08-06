from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Organizer(models.Model):
    name= models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    phone= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)
    date_registered= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
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
    price= models.IntegerField( null=True)
    start_date = models.DateTimeField(null= True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(null=True)
    is_paid = models.BooleanField(default=False, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Registration for {self.event.title} by {self.user}"


class EventFeedback(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    rating = models.PositiveIntegerField(choices=((1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')),null=True)
    feedback = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return f"Feedback for {self.event.title} by {self.name}"
    
