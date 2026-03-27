import sys
import os
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_backend.settings')
django.setup()

from listings.models import Property

def list_properties():
    properties = Property.objects.all()
    print(f"Total properties: {properties.count()}")
    for p in properties:
        print(f"ID: {p.id} | Slug: {p.slug} | Name: {p.name} | Rent: '{p.rent}' | Rent Amount: {p.rent_amount}")

if __name__ == "__main__":
    list_properties()
