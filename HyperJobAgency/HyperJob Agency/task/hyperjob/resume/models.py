from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Resume(models.Model):
    author = models.ForeignKey(User, related_name='resume', on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)

    class Meta:
        app_label = 'resume'
