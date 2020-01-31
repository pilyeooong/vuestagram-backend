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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} - {}'.format(self.caption, self.location)

    @property
    def like_count(self):
        return self.likes.all().count()
    
    @property
    def comment_count(self):
        return self.comments.all().count()


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                               on_delete=models.CASCADE)
    photo = models.ForeignKey(Post, null=True, related_name='likes',
                              on_delete=models.CASCADE)

    def __str__(self):
        return 'User : {} , Photo : {}'.format(self.author.username,
                                               self.photo.caption)


class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                               on_delete=models.CASCADE)
    photo = models.ForeignKey(Post, null=True, related_name='comments',
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
