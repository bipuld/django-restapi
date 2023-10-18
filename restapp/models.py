from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    is_user1 = models.BooleanField(default=False)

    class Meta:
        db_table = "student"  # Set the table name for the Student model
        managed=False