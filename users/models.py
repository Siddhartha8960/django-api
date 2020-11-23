from djongo import models
from django.utils.timezone import now

# Create your models here.


class User(models.Model):
    _id     = models.ObjectIdField()
    name    = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created = models.DateTimeField(default=now)


    def __str__(self):
        return self.name



#         Points - 

# 1- auth module (complete)