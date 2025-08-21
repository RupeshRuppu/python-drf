from django.db import models


# Create your models here.
class Student(models.Model):

    class Meta:
        db_table = "students"

    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name
