from django.db import models
from django.contrib.auth import get_user_model
import datetime
# Create your models here.
User = get_user_model()
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User')
    title=models.CharField(max_length=1020,verbose_name='Title')
    media=models.FileField(verbose_name='Files Upload',upload_to='assets',null=True)
    status=models.BooleanField(default=True,verbose_name='Status')
    hates=models.IntegerField(default=0,verbose_name='Hates')
    views=models.IntegerField(default=0,verbose_name='Views')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Created at',null=True, blank=True)
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Updated at',null=True, blank=True)
    def __str__(self):
        return f"{self.title} --> {self.user}"