from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50,unique=True)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class comment(models.Model):
    id=models.IntegerField(primary_key=True)
    comment=models.CharField(max_length=256)
    blog_id=models.ForeignKey(blog,on_delete=models.CASCADE)
