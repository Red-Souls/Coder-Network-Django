from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    userId = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = 'profile', default = 'profile/unknown_user.png')
    description = models.TextField(null = True, blank = True)

    def __str__(self):  
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    authorProfile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    title = models.CharField(max_length = 116)
    content = models.TextField()
    headerImg = models.ImageField(upload_to = 'post', blank = True, null = True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    authorProfile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
