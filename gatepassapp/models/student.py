from django.db import models
from django.contrib.auth.models import User
import random
from phonenumber_field.modelfields import PhoneNumberField
class Student(models.Model):
    application_id = models.CharField(max_length=10, unique=True, blank=True)
    Name = models.CharField(max_length = 200)
    Rollnumber = models.CharField(max_length =100)
    phone = PhoneNumberField(blank=True, null=True)
    email=models.EmailField(max_length=100, default='test@gmail.com')
    Department = models.CharField(max_length = 100)
    Infromation = models.TextField()
    rejected= models.BooleanField(default=False)
    staff_approval = models.BooleanField(default=False)
    hod_approval = models.BooleanField(default=False)
    warden_approval = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.application_id:
            # Generate a random 6-digit number
            random_number = random.randint(100000, 999999)
            self.application_id = f'sona{random_number}'

        super().save(*args, **kwargs)
   