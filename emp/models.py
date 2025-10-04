from django.db import models

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=10)
    emp_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    emp_working = models.BooleanField(default=True)
    emp_department = models.CharField(max_length=100)
    emp_address = models.TextField(max_length=300)

    def __str__(self):
        return self.name