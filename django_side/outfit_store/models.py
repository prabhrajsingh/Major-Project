from statistics import mode
from django.db import models

# Create your models here.
# class store(models.Model):
#     Id = models.AutoField(primary_key= True) #this is by default added
#     User_name = models.TextField()
#     Timestamp = models.DateTimeField(auto_now_add = True) 
#     Updated = models.DateTimeField(auto_now = True)

#     def __str__(self):
#         return self.User_name



class outfit_upload(models.Model):
    User_name = models.CharField(max_length=100)
    Timestamp = models.DateTimeField(auto_now_add = True) 
    Updated = models.DateTimeField(auto_now = True)
    dress_name = models.CharField(max_length=50)
    dress = models.ImageField(upload_to='dresses/')

    def __str__(self):
        return self.dress_name