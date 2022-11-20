from django.shortcuts import render
from .models import Bird, BirdImages
from .serializers import BirdSerializer, BirdImageSerializer

from rest_framework.viewsets import (GenericViewSet, ModelViewSet,
                                     ReadOnlyModelViewSet)


class BirdViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Bird.objects.prefetch_related('bird_images').all()
    serializer_class = BirdSerializer


class BirdImageViewSet(ModelViewSet):
    serializer_class = BirdImageSerializer

    def get_serializer_context(self):
        return {'bird_id': self.kwargs['bird_pk']}

    def get_queryset(self):
        return BirdImages.objects.filter(bird_id=self.kwargs['bird_pk'])


