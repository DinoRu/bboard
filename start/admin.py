from django.contrib import admin
from .models import Artist, Albums, Contact, Booking
# Register your models here.

admin.site.register(Contact)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['contact', 'album', 'created_at', 'contacted']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', ]

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = ['title', 'reference', 'created', 'available']
    list_filter = ['available', 'created']
    list_editable = ['available']