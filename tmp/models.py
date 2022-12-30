from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid 



class extendedUser(models.Model):
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content_upper_para = RichTextField()
    content_lower_para = RichTextField(default="")
    posted_date = models.DateTimeField(auto_now_add=True)
    postedBy = models.CharField(max_length=50)
    blogImage = models.ImageField(upload_to="blog/images",default="")
    authorImage = models.ImageField(upload_to="author/images",default="")
    aboutAuthor = models.CharField(max_length=1000,default="")

class Project(models.Model):
    head = models.CharField(max_length=100)
    content = RichTextField(max_length=5000)
    posted_date_project = models.DateTimeField(auto_now_add=True)
    postedBy_project = models.CharField(max_length=50)
    projectImage = models.ImageField(upload_to="blog/images",default="")

class New_Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    sub = models.CharField(max_length=50)
    contact= models.IntegerField()
    dob = models.DateField(max_length=50)
    When_contacted = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_teacher = models.CharField(max_length=100)
    Features_of_courses = RichTextField(default="")
    posted_date = models.DateTimeField(auto_now_add=True)
    fees = models.CharField(max_length=50)
    course_image = models.ImageField(upload_to="course/images",default="")
    course_teacher_image = models.ImageField(upload_to="courseTeacher/images",default="")
    aboutTeacher = models.CharField(max_length=1000,default="")

class Paid_Student(models.Model):
    username = models.EmailField(max_length=150)
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    course_name = models.CharField(max_length=150)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False,)
    purchased_date = models.DateTimeField(auto_now_add=True)

class Story(models.Model):
    story_image = models.ImageField(upload_to="story/images",default="")
    brief_content = RichTextField(default="")
    story_by = models.CharField(max_length=100)
# Create your models here.

class Certi(models.Model):
    certi_id=models.CharField(max_length=20)
    cert_name = models.CharField(max_length=150)
    cert_for = models.CharField(max_length=200)
    cert_collegeName = models.CharField(max_length=250)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.certi_id


