from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    password = models.TextField(blank=True)
    url = models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.user.username
class submit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    lover_name = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.user.username
    