from django.db import models
from django.contrib.auth.models import User
# from .models import (
#     Categories
# )

from categories.models import Categories


# Create your models here.

class Videos(models.Model):
    video_title = models.CharField(max_length=50)
    video_description = models.TextField()
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
