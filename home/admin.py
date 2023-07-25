from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Organizer)
admin.site.register(Client)
admin.site.register(Event)
admin.site.register(EventRegistration)
