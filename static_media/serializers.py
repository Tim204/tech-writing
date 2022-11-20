from .models import Bird, BirdImages
from rest_framework import serializers


class BirdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdImages
        fields = ['id', 'bird_image']


class BirdSerializer(serializers.ModelSerializer):
    bird_images = BirdImageSerializer(read_only=True)

    class Meta:
        model = Bird
        fields = ['id', 'name', 'family', 'bird_images']
