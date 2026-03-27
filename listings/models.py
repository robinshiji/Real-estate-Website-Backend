from django.db import models
import uuid

class Property(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Pending', 'Pending'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('Full Property', 'Full Property'),
        ('Room', 'Room'),
    ]

    id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, max_length=100)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')
    postcode = models.CharField(max_length=20, blank=True, null=True)
    rent = models.CharField(max_length=100, blank=True, null=True, help_text="Monthly rent (e.g., £2,500)")
    moving_date = models.DateField(blank=True, null=True)
    viewing_time = models.CharField(max_length=255, blank=True, null=True, help_text="Available viewing times (e.g., After 6 PM)")
    furnished_status = models.CharField(
        max_length=50, 
        choices=[('Furnished', 'Furnished'), ('Unfurnished', 'Unfurnished'), ('Part-Furnished', 'Part-Furnished')],
        default='Unfurnished'
    )
    property_type = models.CharField(
        max_length=50,
        choices=PROPERTY_TYPE_CHOICES,
        default='Full Property'
    )
    rent_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Numeric rent for filtering")
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    video = models.FileField(upload_to='property_videos/', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically populate rent_amount from rent string if not provided
        if not self.rent_amount and self.rent:
            import re
            # Extract numbers and decimal points
            numeric_str = ''.join(re.findall(r'[0-9.]+', self.rent.replace(',', '')))
            if numeric_str:
                try:
                    self.rent_amount = float(numeric_str)
                except ValueError:
                    pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.property.name}"
