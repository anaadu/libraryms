from django.shortcuts import render,redirect
from django.http import HttpResponse
from libapp.models import Book
from libapp.models import IssueBooks
from libapp.forms import EmpFormClass,BookForm,IssueBooksForm,UserRegister
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def adminlogin(request):
        
            return redirect('/admn')
    
        


    






def addbook(request):
    #return render(request,'addbook.html')
    user_id=request.user.id
    #print("Logged in user ID:",user_id)
    if request.method == 'POST':
        name=request.POST['bname']
        cat=request.POST['cat']
        author=request.POST['author']
        price=request.POST['amt']
        status=request.POST['status']

        p=Book.objects.create(name=name,cat=cat,author=author,price=price,status= status,uid=user_id)
        print(p)
        p.save()
        return redirect('/admn')
        #return HttpResponse("record successfully inserted")

    else:
        print("GET request in POST section")
        return render(request,'addbook.html')



def adminpage(request):
    user_id=request.user.id
    #qset=Book.objects.all()
    qset=Book.objects.filter(uid=user_id)
    content={}
    content['data']=qset
    return render(request,'admin.html',content)

def delete(request,rid):
    p=Book.objects.filter(id=rid)
    p.delete()
    return redirect('/admn')

def edit(request,rid):

    if request.method == 'POST':
        name=request.POST['bname']
        cat=request.POST['cat']
        author=request.POST['author']
        price=request.POST['amt']
        status=request.POST['status']

        p=Book.objects.filter(id=rid)
        p.update(name=name,cat=cat,author=author,price=price,status=status)
        return redirect('/admn')

    else:
        p=Book.objects.filter(id=rid)
        content={}
        content['data']=p
        return render(request,'edit.html',content)



def Issuebook(request):
    user_id=request.user.id
    if request.method == 'POST':
        Student_name=request.POST['sname']
        #Student_id=request.POST['sid']
        book_name=request.POST['bname']
        Issue_date=request.POST['idate']

        p=IssueBooks.objects.create(Student_name=Student_name,book_name=book_name,issued_date=Issue_date,uid=user_id)
        p.save()
        return redirect('/issuedbook')
        #return HttpResponse("record successfully inserted")
    
    else:
        print("get request in post section")
        return render(request,'issue_book.html')


    #return render(request,'issue_book.html')


def Issued_book(request):
    user_id=request.user.id
    #iset=IssueBooks.objects.all()
    iset=IssueBooks.objects.filter(uid=user_id)
    content={}
    content['data']=iset
    return render(request,'issued_book.html',content)


def deleteissuebook(request,rid):
    p=IssueBooks.objects.filter(id=rid)
    p.delete()
    return redirect('/issuedbook')

def statfilter(request,sf):
    p=Book.objects.filter(status=sf)
    content={}
    content['data']=p
    return render(request,'admin.html',content)

def catfilter(request,cf):
    p=Book.objects.filter(cat=cf)
    content={}
    content['data']=p
    return render(request,'admin.html',content)


def sortfilter(request,x):
    if x == '0':
        p=Book.objects.order_by('price')
    else:
        p=Book.objects.order_by('-price')
    
    content={}
    content['data']=p
    return render(request,'admin.html',content)



def setcookie(request):
    res=render(request,'setcookie.html')
    res.set_cookie('name','shital')
    res.set_cookie('rollno',213)

    return res

def getcookie(request):
    name=request.COOKIES['name']
    rnum=request.COOKIES['rollno']

    content={}
    content['name']=name
    content['rolnum']=rnum

    return render(request,'getcookie.html',content)


def setsession(request):
    request.session['name']="Shital pratik rane"
    return render(request,'setsession.html')


def getsession(request):
    content={}
    content['name']=request.session['name']

    return render(request,'getsession.html',content)



def django_form(request):
    if request.method=='POST':
        name=request.POST['empname']
        mob=request.POST['mobile']
        dept=request.POST['department']
        dt=request.POST['date_of_joining']
        
        # print(name)
        # print(mob)
        # print(dept)
        # print(dict)





    else:

        dfobj=EmpFormClass()
        #print(dfobj)
        content={}
        content['form']=dfobj
        return render(request,'empform.html',content)



def modelform(request):
    if request.method=="POST":
        pass
    else:
        mfobj=BookForm()
        #print(mfobj)
        content={}
        content['form']=mfobj
        return render(request,'addbookmodel.html',content)
    

def modelform2(request):
    if request.method=="POST":
        pass
    else:
        mfobj=IssueBooksForm()
        #print(mfobj)
        content={}
        content['form']=mfobj
        return render(request,'issuebookmodel.html',content)
        


def user_register(request):

    content={}
    if request.method=="POST":

        regfm=UserRegister(request.POST)
        #print(regfm)
        #print(regfm.is_valid())
        if regfm.is_valid():
            regfm.save()

            content['msg']="User Register Successfully"
            return render(request,'registersuccess.html',content)

    else:
        #regfm=UserCreationForm()
        #print(regfm )
        regfm=UserRegister()
        content={}
        content['regfm']=regfm
        return render(request,'register.html',content)  
    

def user_login(request):
    if request.method=="POST":
        logfm=AuthenticationForm(request=request,data=request.POST)
        #print(logfm)
        if logfm.is_valid():
            uname=logfm.cleaned_data['username']
            upass=logfm.cleaned_data['password']

            #print(uname)
            #print(upass)
            res=authenticate(username=uname,password=upass)
            #print(res)
            if res:
                login(request,res)
                return redirect('/admn')
            
             

    else:
        logfm=AuthenticationForm()
        #print(logfm)
        content={}
        content['form']=logfm
        return render(request,'login.html',content)