from django.contrib.auth.models import User
from django.db import models


class Short(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shorts')
    username = models.CharField('Username', max_length=100, default='')
    profile_photo = models.CharField('Profile Photo (URL)', max_length=1000, default='')
    caption = models.CharField('Caption', max_length=500, default='')
    video = models.FileField('Video', upload_to='tube_videos/', default='')

    def __str__(self):
        return f'{self.user.username} short object ({self.id})'
