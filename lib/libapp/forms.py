from django import forms
from libapp.models import Book,IssueBooks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmpFormClass(forms.Form):
    empname=forms.CharField(max_length=50)
    mobile=forms.IntegerField()
    department=forms.CharField(max_length=50)
    date_of_joining=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))


class BookForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    cat=forms.CharField(max_length=200)
    author=forms.CharField(max_length=200)
    price=forms.FloatField()
    status=forms.CharField(max_length=100)

    class Meta:
        model=Book
        fields=['name','cat','author','price','status']

class IssueBooksForm(forms.ModelForm):
     Student_name=forms.CharField(max_length=100)
     book_name=forms.CharField(max_length=200)
     issued_date = forms.DateField()


     class Meta:
         model=IssueBooks
         fields=['Student_name','book_name','issued_date']




class UserRegister(UserCreationForm):
    class Meta:
        model=User

        fields=['username','first_name','last_name','email']