from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    draft=models.BooleanField(default=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    publish_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    image=models.ImageField(upload_to='photo')
    tags = TaggableManager()
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='post_category')


    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_author')
    publish_date=models.DateTimeField(auto_now=True)
    content=models.TextField(max_length=500)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment_post')

    def __str__(self):
        return str(self.post)
    
    
