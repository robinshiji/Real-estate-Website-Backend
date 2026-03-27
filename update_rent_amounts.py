import sys
import os
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_backend.settings')
django.setup()

from listings.models import Property

def update_all_rent_amounts():
    properties = Property.objects.all()
    count = 0
    for p in properties:
        # Saving triggers the new save() logic with rent_amount population
        p.save()
        count += 1
    print(f"Successfully updated {count} properties.")

if __name__ == "__main__":
    update_all_rent_amounts()
