from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name='posts')
    photo = ProcessedImageField(upload_to='images/%Y/%m/%d',
                                default='images/no_image.png',
                                processors=[ResizeToFill(600, 600)],
                                format='JPEG', options={'quality': 90}
                                )
    location = models.CharField(max_length=140)
    caption = models.CharField(max_length=140)


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    photo = models.ForeignKey(Post, null=True, related_name='likes')
