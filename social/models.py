from django.contrib.auth.models import User
from django.db import models


class Neighborhood(models.Model):
    name = models.CharField('Name', max_length=200, unique=True)
    state = models.CharField('State', max_length=100, default='')
    latitude = models.FloatField('Latitude', default=0.0)
    longitude = models.FloatField('Longitude', default=0.0)

    def __str__(self):
        return f'{self.name} neighborhood object ({self.id})'


class NeighborhoodFollower(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighborhood_followers')
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighborhoods_followed')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.SET_NULL, null=True, related_name='neighborhood_posts')
    post_text = models.TextField('Post Text', max_length=1000, default='')
    country = models.CharField('Country', max_length=100, default='')
    state = models.CharField('State', max_length=100, default='')
    city = models.CharField('City', max_length=100, default='')
    area_address = models.CharField('Area Address', max_length=200, default='')
    longitude = models.FloatField('Longitude', default=0.0)
    latitude = models.FloatField('Latitude', default=0.0)

    def __str__(self):
        return f"{self.user.username} post object ({self.id})"


class Media(models.Model):
    media = models.FileField('Media', upload_to='post_media/', default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media_list')

    class Meta:
        verbose_name_plural = 'Media'


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_liked')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_list')
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment_text = models.TextField('Comment Text', max_length=500, default='')


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_liked')


class ConnectionRequest(models.Model):
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_sent_by')
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_sent_to')

    def __str__(self):
        return f"{self.sent_by} <==> {self.sent_to} connection request object ({self.id})"


class Connection(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_one_connections')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_two_connections')

    def __str__(self):
        return f"{self.user_one} <==> {self.user_two} connection object ({self.id})"
