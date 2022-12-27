from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class Department(models.Model):
    dep_name = models.CharField(max_length=255)

    def __str__(self):
        return self.dep_name


class Role(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=12)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


leaves_status = (
    ("Approved","Approved"),("Pending","Pending"),("Rejected","Rejected")
    )
class Leaves(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    leave_from_date = models.DateField(default=datetime.date.today)
    leave_to_Date = models.DateField(default=datetime.date.today)
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices= leaves_status, default="Pending")

