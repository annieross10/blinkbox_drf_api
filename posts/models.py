from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qohjd5', blank=True
    )
    like = models.ManyToManyField(
        User, related_name='post_likes', blank=True)
    love = models.ManyToManyField(
        User, related_name='post_loves', blank=True)
    laugh = models.ManyToManyField(
        User, related_name='post_laughs', blank=True)

    image_filter = models.CharField(
        max_length=32, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def number_of_like(self):
        return self.like.count()

    def number_of_love(self):
        return self.love.count()

    def number_of_laugh(self):
        return self.laugh.count()