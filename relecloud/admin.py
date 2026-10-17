from django.contrib import admin
from .models import Destination, Cruise, InfoRequest

# Register your models here.
admin.site.register(Destination)
admin.site.register(Cruise)
admin.site.register(InfoRequest)
