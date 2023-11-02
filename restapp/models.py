import uuid
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def uuid_generate():
    return uuid.uuid4().hex

class BaseModel(models.Model):
    referenceid=models.CharField(unique=True,default=uuid_generate,max_length=32)
    created_by=models.ForeignKey(User,on_delete=models.PROTECT,null=True,db_column="created_by",related_name="+")
    created_at=models.DateField(auto_now_add=True)
    updated_by=models.ForeignKey(User,on_delete=models.PROTECT,null=True,db_column="updated_by",related_name="+")
    is_delete=models.BooleanField(default=False)
    
    class Meta:
      abstract=True
    
    
class Student(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_num=models.CharField(max_length=15)
    roll_number=models.IntegerField()


    class Meta:
        db_table = "student"  # Set the table name for the Student model


class Course(BaseModel):
    name=models.CharField(max_length=150)
    pub_date=models.DateField(null=True)
    page_num=models.IntegerField()      
    
    class Meta:
        db_table = 'courses'
    
    