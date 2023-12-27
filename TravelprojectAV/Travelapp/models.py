from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=55)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class btable(models.Model):
    date=models.IntegerField()
    month=models.TextField()
    desc1=models.CharField(max_length=50)
    desc2=models.CharField(max_length=50)
    desc3=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')

