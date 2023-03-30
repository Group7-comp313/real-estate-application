from django.db import models
from  datetime import datetime
class Contact(models.Model):
    listing=models.CharField(max_length=200)
    listing_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=True)
    realtor_email=models.EmailField(default=None)

    def __str__(self):
        return self.name




# Create your models here.
