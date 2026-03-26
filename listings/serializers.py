from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def get_gallery(self, obj):
        # Only use uploaded PropertyImage URLs
        uploaded_images = []
        request = self.context.get('request')
        
        for img_obj in obj.images.all():
            if img_obj.image:
                url = img_obj.image.url
                if request:
                    url = request.build_absolute_uri(url)
                uploaded_images.append(url)
        
        return uploaded_images

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = instance.slug
        if instance.image:
            request = self.context.get('request')
            if request:
                representation['image'] = request.build_absolute_uri(instance.image.url)
        
        if instance.video:
            request = self.context.get('request')
            if request:
                representation['video'] = request.build_absolute_uri(instance.video.url)
        return representation
