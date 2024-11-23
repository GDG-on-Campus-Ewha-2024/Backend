from django.db import models

# Create your models here.
class Trip(models.Model):
    title = models.CharField(max_length=225, unique=True)
    addr1 = models.CharField(max_length=255)
    addr2 = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True)
    img = models.URLField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.title
    