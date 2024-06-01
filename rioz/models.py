from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.text import Truncator


# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=75)
    avatar = models.ImageField(upload_to='static/images/avatars/')
    cover_pic = models.ImageField(blank=True, null=True, upload_to='static/images/cover_pic/')
    address = models.CharField(max_length=255)
    email = models.EmailField()
    born_date = models.DateField(blank=True, null=True)
    contact = models.CharField(
        max_length=13,
        validators=[MinLengthValidator(10), MaxLengthValidator(13)]
    )
    cv = models.FileField(upload_to='static/cv/', blank=True, null=True)

    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    

class Education(models.Model):
    board = models.CharField(max_length=45)
    year = models.CharField(max_length=10)
    institution = models.CharField(max_length=100)

    def __str__(self):
        return self.board
    

class Experience(models.Model):
    company_name = models.CharField(max_length=65)
    logo = models.ImageField(upload_to='static/images/company_logo')
    job_desc = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Set is_complete to True if end_date is present, otherwise False
        if self.end_date:
            self.is_complete = True
        else:
            self.is_complete = False
        # Call the original save() method
        super().save(*args, **kwargs)


    def __str__(self):
        return self.company_name
    
    
class About(models.Model):
    short_bio = models.CharField(max_length=100)
    intro = models.CharField(max_length=350)
    about_me = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.short_bio
    


class Skills(models.Model):
    skill_id = models.CharField(auto_created=True, max_length=10, editable=False)
    skill_name = models.CharField(max_length=65)
    skill_image = models.ImageField(upload_to='static/images/skills/')
    skill_experience = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
        
    def __str__(self):
        return self.skill_name
    

class Service(models.Model):
    service_name = models.CharField(max_length=60, null=True)
    service_info = models.TextField(null=True)

    def __str__(self):
        return self.service_name
    


class Clients(models.Model):
    client_id = models.CharField(max_length=8, auto_created=True, editable=False)
    client_name = models.CharField(max_length=50)
    client_logo = models.ImageField(upload_to='static/images/clients/')
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.client_name

    def delete(self, *args, **kwargs):
        if self.client_logo:
            if os.path.isfile(self.client_logo.path):
                os.remove(self.client_logo.path)
        super().delete(*args, **kwargs)

@receiver(post_delete, sender=Clients)
def delete_client_logo(sender, instance, **kwargs):
    if instance.client_logo:
        if os.path.isfile(instance.client_logo.path):
            os.remove(instance.client_logo.path)



class Blog(models.Model):
    blog_id = models.CharField(max_length=15, editable=False, auto_created=True)
    blog_topic = models.CharField(max_length=150)
    blog_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_topic
    
    def get_excerpt(self, num_chars=100):
        return Truncator(self.blog_text).chars(num_chars)
    

class Comments(models.Model):
    comment_name = models.CharField(max_length=55, null=True, blank=True)
    comment_text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_text
