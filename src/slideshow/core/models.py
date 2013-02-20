from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Slideshow(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    rendered = models.TextField()
    
    def __unicode__(self):
        return self.title