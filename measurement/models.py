from django.db import models

from datetime import datetime

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

class Measurement(models.Model):
    sensor_id = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='measurement_images/', null=True, blank=True)