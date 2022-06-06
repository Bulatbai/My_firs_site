
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL,
                null=True, blank=True
                )
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    create_update = models.DateTimeField(auto_now=True)
    img = models.ImageField(null=True)


    def __str__(self):
        return self.name



# Create your models here.
