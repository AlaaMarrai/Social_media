from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid

User  = get_user_model()

# Create your models here.
# class Profile(models.Model):
#     profile_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_user = models.IntegerField()
#     bio = models.TextField(blank=True)
#     profile_pic = models.ImageField(upload_to= 'profile_images', default='blank-profile-picture.png')
#     location = models.CharField(max_length=100, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
    
#     def __str__(self):
#         return self.user.username

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(null=True, blank=True, default=None)
    profile_pic = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id_user is None:
            self.id_user = self.user.id
        super(Profile, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username    

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image_url = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(default=datetime.now)  
    num_likes = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):

        super(Post, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username   
 
 
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default=None)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

        
    def __str__(self):
        return self.user.username  
 
class Like(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):

       super(Like, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username 
   
class FollowersCount(models.Model):
    follower =  models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):

       super(FollowersCount, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username 
       
           