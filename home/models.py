from django.db import models

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
    CATEGORY=(
        ('Concerts', 'Concerts'),
        ('Classes & Workshops', 'Classes & Workshops'),
        ('Corporate Events', 'Corporate Events'),
        ('Festivals & Fairs', 'Festivals & Fairs'),
    )


    event_name = models.CharField(max_length=200, null=True)
    name_of_organizer= models.ForeignKey(Organizer, null=True, on_delete= models.SET_NULL)
    category= models.CharField(max_length=200, null=True, choices=CATEGORY)
    place_of_event = models.CharField(max_length=200, null=True)
    description= models.CharField(max_length=200, null=True, blank=True)
    price=models.IntegerField(null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.event_name
    
