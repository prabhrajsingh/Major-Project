from statistics import mode
from django.db import models

# Create your models here.
class store(models.Model):
    Id = models.AutoField(primary_key= True) #this is by default added
    User_name = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add = True) 
    Updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.User_name
