from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ParkingSpace

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_hour', 'is_free', 'owner')





from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'parking_space', 'start_time', 'end_time', 'total_price', 'is_paid')