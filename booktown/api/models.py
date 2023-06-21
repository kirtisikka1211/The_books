from django.db import models

# Create your models
class Book(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    no_of_books = models.IntegerField()
    username= models.CharField(max_length=100)
    pre_primary=models.IntegerField(default=0)
    primary=models.IntegerField(default=0)
    secondary=models.IntegerField(default=0)
    senior_secondary=models.IntegerField(default=0)
    def __str__(self):
        return self.full_name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.IntegerField()
    query= models.TextField(max_length=600, default="Null")
    type=models.CharField(max_length=100)
    ngo=models.CharField(max_length=100, default="Null")
    website=models.CharField(max_length=100, default="Null")
    address = models.CharField(max_length=100, default="Null")
    org=models.CharField(max_length=100, default="Null")
    def __str__(self):
        return self.name