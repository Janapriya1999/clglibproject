from email.policy import default
from django.db import models

# Create your models here.
class studentRegisterModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    student_fullname=models.CharField(help_text='student_fullname',max_length=100,default=True)
    student_branch=models.CharField(help_text='student_branch',max_length=100,default=True)
    student_year=models.CharField(help_text='student_year',max_length=100,default=True)
    student_email=models.EmailField(help_text='student_email',max_length=100,default=True)
    student_password=models.CharField(help_text='student_password',max_length=100,null=True)
    student_id=models.CharField(help_text='student_id',max_length=100,null=True)
    student_photo=models.ImageField(upload_to='images/',null = True)
    student_status=models.CharField(default="pending",max_length=50)
    class meta:
        db_table='student_details'

class StudentFeedbackModel(models.Model):
    student_id=models.ForeignKey(studentRegisterModel,models.CASCADE,null=True)
    rating3=models.CharField(help_text='rating3',max_length=200,null=True)
    text=models.CharField(help_text='text',max_length=200,null=True)
    sentiment=models.CharField(help_text='sentiment',max_length=700,null=True)
    class meta:
        db_table='student_feedback'
