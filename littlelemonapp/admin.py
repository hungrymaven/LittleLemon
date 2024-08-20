from django.contrib import admin
from .models import Reserve, Booking, Book
# Register your models here.

admin.site.register(Reserve)
admin.site.register(Booking)
admin.site.register(Book)