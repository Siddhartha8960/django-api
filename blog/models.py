from djongo import models
from django.utils.timezone import now

# Create your models here.


class Blog(models.Model):
    _id          = models.ObjectIdField()
    blog_name    = models.CharField(max_length=50)
    created = models.DateTimeField(default=now)


    def __str__(self):
        return self.blog_name
