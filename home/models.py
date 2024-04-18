from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveBigIntegerField()


    def __str__(self):
        return self.name
