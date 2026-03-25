from django.db import models
import uuid

class Property(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Pending', 'Pending'),
    ]

    id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, max_length=100)
    badge = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)  # String to store formatted price like "$32,500,000"
    priceNote = models.CharField(max_length=255)
    beds = models.IntegerField()
    baths = models.IntegerField()
    sqft = models.CharField(max_length=50)
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    description = models.TextField()
    features = models.JSONField(default=list)
    viewing_time = models.CharField(max_length=255, blank=True, null=True, help_text="e.g., Every Sunday 10 AM - 4 PM")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.property.name}"
