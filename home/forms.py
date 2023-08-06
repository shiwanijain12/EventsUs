from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


#class CreateUserForm(UserCreationForm):
    #class Meta:
        #model= User
        #fields=['username', 'email', 'password1', 'password2']

#class CreateEvent(ModelForm):
    #class Meta:
        #model= Event
        #fields='__all__'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Organizer, Client

class OrganizerRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ClientRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ('event','user', 'email')


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'category', 'start_date', 'end_date', 'price')


class EventFeedbackForm(forms.ModelForm):
    class Meta:
        model = EventFeedback
        fields = ('name', 'email', 'rating', 'feedback')

