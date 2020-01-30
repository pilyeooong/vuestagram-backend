from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, 
                              verbose_name='email address')
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
        (GENDER_OTHER, '기타'),
    )
    profile_image = models.ImageField(upload_to='profile', blank=True)
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    introduction = models.TextField(blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='following', blank=True)

    def __str__(self):
        return self.username

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()
