from django.contrib import admin
from .models import Reserve, ManualReservation
# Register your models here.

admin.site.register(Reserve)
admin.site.register(ManualReservation)