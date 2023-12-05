from django.urls import path
from libapp import views

urlpatterns = [
    path('addbook',views.addbook),
    path('admn',views.adminpage),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('home',views.homepage),
    path('adminlogin',views.adminlogin),
    path('issuebook',views.Issuebook),
    path('issuedbook',views.Issued_book),
    path('delete1/<rid>',views.deleteissuebook),
    path('statfilter/<sf>',views.statfilter),
    path('catfilter/<cf>',views.catfilter),
    path('sort/<x>',views.sortfilter),
    path('setcookie',views.setcookie),
    path('getcookie',views.getcookie),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('djforms',views.django_form),
    path('modelform',views.modelform),
    path('modelform2',views.modelform2),
    path('register',views.user_register),
    path('login',views.user_login),

]
 