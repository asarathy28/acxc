from django.conf import settings
from django.db import models

# Create your models here.

class ShortRoutes(models.Model):
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    map_src = models.TextField()
    description = models.TextField()

    def __str__ (self):
        return self.name

class MediumRoutes(models.Model):
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    map_src = models.TextField()
    description = models.TextField()

    def __str__ (self):
        return self.name

class LongRoutes(models.Model):
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    map_src = models.TextField()
    description = models.TextField()

    def __str__ (self):
        return self.name

class LongRunRoutes(models.Model):
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    map_src = models.TextField()
    description = models.TextField()

    def __str__ (self):
        return self.name

class DestinationRoutes(models.Model):
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    map_src = models.TextField()
    description = models.TextField()

    def __str__ (self):
        return self.name
