from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
