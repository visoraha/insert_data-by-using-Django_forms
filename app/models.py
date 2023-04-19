from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=100)
    name=models.CharField(max_length=100)
    mbno=models.IntegerField()
    email=models.EmailField()
    def __str__(self) -> str:
        return self.name
class Course(models.Model):
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    cname=models.CharField(max_length=100)
    marks=models.IntegerField()