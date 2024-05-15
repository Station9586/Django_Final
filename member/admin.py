from django.contrib import admin
from .models import Reservations
# Register your models here.

class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Date', 'Time', 'people', 'space')
    ordering = ('Date', )

admin.site.register(Reservations, ReservationsAdmin)