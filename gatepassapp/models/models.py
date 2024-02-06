from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES=[
        ('teacher','Teacher'),
        ('student','Student'),
        ('hod','HOD'),
        ('warden','Warden'),
        ('admin','Admin'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    def __str__(self):
        return self.username