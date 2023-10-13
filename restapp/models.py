from django.db import models



class Basemodel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Student(Basemodel):
    is_user1 = models.BooleanField(default=False)

    class Meta:
        db_table = "student"  # Set the table name for the Student model
        managed=False
class Teacher(Basemodel):
    is_user1 = models.BooleanField(default=False)

    class Meta:
        db_table = "teacher"  # Set the table name for the Teacher model

    is_user1=models.BooleanField(default=False)
    
    class META:
        db_table="teacher" 