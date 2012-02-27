from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Product(models.Model):
    uuid = models.CharField(max_length=36, null=True, blank=True, \
        default=str(uuid4()))
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
