from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_num=models.CharField(max_length=15)


    class Meta:
        db_table = "student"  # Set the table name for the Student model
        managed=False