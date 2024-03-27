from django.db import models

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100, verbose_name='Full Name')
    email = models.CharField(max_length=100 ,verbose_name="Email")
    contact = models.CharField(max_length=100, verbose_name="Contact")
    age = models.IntegerField(verbose_name="Age")
    address = models.CharField(max_length=100,verbose_name="Address")
    academicLevel = models.CharField(max_length=100,verbose_name="Academic Level")
    university = models.CharField(max_length=100,verbose_name="University")
    fieldStudy = models.CharField(max_length=100,verbose_name="Field Study")
    studyDestination = models.CharField(max_length=100,verbose_name="Study Destination")
    enrollment = models.CharField(max_length=100, verbose_name="Enrollment")
    languageProficiency = models.CharField(max_length=100,verbose_name="Language Proficiency")