from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Categories(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    date_time = models.DateTimeField(timezone.now)

