from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='products', null=True)
    
    def __unicode__(self):
        return self.name
