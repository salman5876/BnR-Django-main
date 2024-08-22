from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from products.models import *

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0', related_name='user_detail')
    Mobile = models.CharField(max_length=18)
    newsLetter=models.BooleanField(default=True)
    email=models.CharField(max_length=255, null=True)
    isAuthenticated=models.BooleanField(default=False)
    SeceretKey=models.CharField(max_length=255, null=True)
    ISConfirmed=models.BooleanField(default=False)
    is_social = models.BooleanField(default=False)
    social_id = models.CharField(max_length=200, null=True, blank=True)
    social_provider = models.CharField(max_length=200, null=True, blank=True)
    snr_uid = models.CharField(max_length=500, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.ImageField('Profile Image', upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Details ({self.id})"


# Downlaod image & save to local media
#

class sendFriends(models.Model):
    email = models.CharField(max_length=255, null=True,unique=True)
    sharedlink=models.CharField(max_length=2000, null=True)

class Subscribers(models.Model):
    email = models.CharField(max_length=255, null=True,unique=True)
    isSend=models.BooleanField(default=False)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return self.email if self.email else ''+' , '+self.isSend if self.isSend else ''+' , '+self.SNR_Date if self.SNR_Date else ''



class Reset_password(models.Model):
    email = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255, null=True)
    Code = models.CharField(max_length=10, null=True)
    isValid=models.BooleanField(default=False)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return self.email if self.email else ''+' , '+self.link if self.link else ''+' , '+self.Code if self.Code else ''+' , '+self.isValid if self.isValid else ''+' , '+self.SNR_Date if self.SNR_Date else ''


class Interst(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')
    SNR_Available = models.CharField(max_length=255, null=True)
    Count = models.IntegerField(default=0,blank=True)
    Product=models.CharField(blank=True,null=True,max_length=500)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return self.SNR_Available