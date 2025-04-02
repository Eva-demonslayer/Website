from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to='static/images/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name