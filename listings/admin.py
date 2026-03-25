from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3  # Show 3 empty slots by default

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'status', 'city', 'viewing_time')
    list_filter = ('status', 'city', 'badge')
    search_fields = ('name', 'location', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PropertyImageInline]
