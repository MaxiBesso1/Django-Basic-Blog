from django.db import models

# Create your models here.

class User(models.Model):
    nickname= models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    personal_description = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='profile_photos',default="image-user.png")

    def __str__(self):
        return "%s / %s / %s /" %(self.nickname,self.password,self.personal_description)
    

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=4000)
    nickname_dad = models.CharField(max_length=20,null=True)
    img = models.ImageField(upload_to="post_files",default="image-user.png")
    category = models.CharField(max_length=50)
    ansewer = models.BooleanField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s / %s / %s / %s / %s / %s /  " %(self.title,self.content,self.img,self.category,self.ansewer,self.date)
    

class Ansewer_Post(models.Model):
    content = models.TextField(max_length=4000)
    id_post_ansewer = models.IntegerField()
    nickname_create = models.CharField(max_length=20,null=True) 
    date= models.DateTimeField(auto_now=True)
