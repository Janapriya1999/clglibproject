from email.policy import default
from pydoc import describe
from django.db import models
from librarianapp.models import *
from studentapp.models import *

# Create your librarianapp models here.

class AddingBooksModel(models.Model):
    book_id=models.AutoField(primary_key=True)
    booktitle=models.CharField(help_text='tit',max_length=100, null=True)
    authorname=models.CharField(help_text='auth',max_length=100)
    department=models.CharField(help_text='dep',max_length=100)
    publisher=models.CharField(help_text='pub',max_length=100)
    edition=models.CharField(help_text='edi',max_length=100)
    descripition=models.TextField(help_text='descripition',null=True)
    bookphoto=models.ImageField(upload_to="images/")
    status=models.TextField(default="pending")
    class meta:
        db_table='AddingBooksdetails'

class ViewBooks (models.Model):
    view_id=models.AutoField(primary_key=True)
    stu_id=models.ForeignKey(studentRegisterModel,on_delete=models.CASCADE,null=True)
    librarian_id=models.ForeignKey(AddingBooksModel,on_delete=models.CASCADE,null=True)
    librarian_status=models.CharField(default="pending",max_length=50)
    return_book_status=models.CharField(default="pending",max_length=50)
    class meta:
        db_table='student_purchased_book'
class return_book(models.Model):
   return_id=models.AutoField(primary_key=True)    
   stu_id=models.CharField(help_text='stu_id',max_length=500,null=True) 
   book_id=models.CharField(help_text='book_id',max_length=500,null=True)
   return_status= models.CharField(default='pending',max_length=500)
   return_count= models.CharField(default='0',max_length=500)
   class meta:
        db_table='student_return_book_details'
