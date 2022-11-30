from email.policy import default
from django.db import models

# Create your adminapp models here.

class addingLibrarianModel(models.Model):
    librarian_id=models.AutoField(primary_key=True)
    librarian_name=models.CharField(help_text='librarian_name',max_length=100)
    librarian_phonenumber=models.BigIntegerField(help_text='librarian_phonenumber')
    librarian_campusname=models.TextField(help_text='librarian_campusname',max_length=100)
    librarian_blockname=models.TextField(help_text='librarian_blockname',max_length=100)
    librarian_email=models.EmailField(help_text='librarian_email',max_length=100)
    librarian_password=models.CharField(help_text='librarian_password',max_length=100)
    librarian_photo=models.ImageField(upload_to="images/")
    status=models.TextField(default="completed")
    class meta:
        db_table='addingLibrariandetails'

