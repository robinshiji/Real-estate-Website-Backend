from rest_framework import generics, filters, permissions
from .models import Property
from .serializers import PropertySerializer

class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'postcode', 'location']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]      # 👀 public
        return [permissions.IsAdminUser()]       # 🔐 admin only


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]      # 👀 public
        return [permissions.IsAdminUser()]       # 🔐 admin only
