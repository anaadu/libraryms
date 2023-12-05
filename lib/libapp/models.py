from django.db import models

# Create your models here.
class Book(models.Model):
    CAT=(('1','Fantacy'),('2','Adventure'),('3','Historical'),('4','Horror'),('5','Triller'))
    STAT=(('1','Active'),('0','Inactive'))
    name=models.CharField(max_length=200,verbose_name="book name")
    cat=models.CharField(max_length=200,verbose_name="category",choices=CAT)
    author=models.CharField(max_length=200,verbose_name="Author name")
    price=models.FloatField()
    status=models.CharField(max_length=100,choices=STAT)
    uid=models.IntegerField()

    def __str__(self):
        return self.name

class IssueBooks(models.Model):

    Student_name=models.CharField(max_length=100,verbose_name="Student name")
    #student_id = models.CharField(max_length=100, blank=True) 
    book_name=models.CharField(max_length=200)
    issued_date = models.DateField()
    uid=models.IntegerField()

    def __str__(self):
        return self.Student_name
    