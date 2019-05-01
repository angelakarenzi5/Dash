from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='gram/', blank=True)
    bio= models.CharField(max_length =1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

def __str__(self):
        return self.user_name
        
def save_profile(self):
        self.save()

class Meta:
        ordering = ['user_name']

class Trucker(models.Model):
        drivers_name = models.CharField(max_length =100)
        trucking_numbers = models.IntegerField()
        state_of_product = models.CharField(max_length =100)

        
def __str__(self):
        return self.user_name
        
def save_trucker(self):
        self.save()

class Meta:
        ordering = ['user_name']