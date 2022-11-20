from django.db import models


class Bird(models.Model):
    name = models.CharField(max_length=100, default="bird")
    family = models.CharField(max_length=100, default="unknown")

    def __str__(self):
        return self.name


class BirdImages(models.Model):
    bird = models.OneToOneField(Bird, on_delete=models.CASCADE, related_name="bird_images")
    bird_image = models.ImageField(upload_to='static_media/images')
