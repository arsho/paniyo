import os
from django.db import models
from django.conf import settings


class Product(models.Model):
    title = models.CharField(max_length=200)
    elements = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(
        default='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Phantom_Open_Emoji_1f379.svg/480px-Phantom_Open_Emoji_1f379.svg.png'
    )
