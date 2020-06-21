from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=155)
    content = models.TextField(max_length=5000)
    auther = models.CharField(max_length=50)
    slug = models.CharField(max_length=500)
    timeStamp = models.DateTimeField(blank=True)
    

    def __str__(self):
        return self.title + ' by ' + self.auther