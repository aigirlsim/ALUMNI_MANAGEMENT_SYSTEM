from django.db import models
from django.contrib.auth.models import AbstractUser



# Create Course and session Model  
  
class CustomUser(AbstractUser):
        USER =(
              
              (1,"Staff"),
              (2,"Alumni"),
        )
        user_type = models.CharField(choices=USER,max_length=50,default=1)
        profile_pic  = models.ImageField(upload_to= 'media/profile_pic')


class Course(models.Model):
        name = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name
        
class Session_Year(models.Model):
        session_start = models.CharField(max_length=100)
        session_end = models.CharField(max_length=100)

        def __str__(self):
            return self.session_start + " " + self.session_end
        
class Insitute(models.Model):
      name = models.CharField(max_length=100)

      def __str__(self):
            return self.name

class Contact(models.Model):
      contact = models.CharField(max_length=100)

      def __str__(self):
            return self.contact
      
class Event(models.Model):
      Title = models.CharField(max_length=100)
      event_img = models.ImageField(upload_to= 'media/event_pic')
      description = models.CharField(max_length=150)
      
      def __str__(self):
            return self.Title

class Alumni(models.Model):
       admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
       gender = models.CharField(max_length=100)
       course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
       session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
       created_at = models.DateTimeField(auto_now_add=True)
       update_at = models.DateTimeField(auto_now=True)

       def __str__(self):
            return self.admin.first_name + "   " + self.admin.last_name
              
class PJob(models.Model):
      Title = models.CharField(max_length=100)
      CompanyName = models.CharField(max_length=100)
      Location = models.CharField(max_length=100)
      description = models.CharField(max_length=150)
      AplicvationDeadline = models.DateTimeField()
      Link = models.URLField(max_length=100)
      
      def __str__(self):
            return self.Title    