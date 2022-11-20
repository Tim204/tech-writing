from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('birds', views.BirdViewSet, basename='birds')

birds_router = routers.NestedDefaultRouter(router, 'birds', lookup='bird')
birds_router.register('bird_images', views.BirdImageViewSet, basename='bird-images')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(birds_router.urls)),
    path('', TemplateView.as_view(template_name='static_media/index.html'))
]