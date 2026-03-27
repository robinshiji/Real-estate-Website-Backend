from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3  # Show 3 empty slots by default

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'status', 'postcode', 'rent', 'rent_amount', 'moving_date', 'viewing_time', 'furnished_status')
    list_filter = ('status', 'furnished_status')
    search_fields = ('name', 'location', 'postcode', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PropertyImageInline]
