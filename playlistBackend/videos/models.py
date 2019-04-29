from django.db import models

# Create your models here.

#from categories.models import Categories


class Videos(models.Model):
    video_title = models.CharField(max_length=50)
    video_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #categories = models.ForeignKey(Categories, related_name='categories', on_delete=models.CASCADE)
    categories = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', related_name='videos', on_delete=models.CASCADE)

