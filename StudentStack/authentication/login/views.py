from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
   return render(request, 'index.html')



def index2(request):
     return render(request, 'index2.html')   

def terms(request):
     return render(request, 'terms.html')


def terms_signup(request):
   return render(request, 'terms_signup.html')



def chemistry_(request):
   return render(request, 'chemistry_.html')

def physics(request):
   return render(request, 'physics.html')


def other_(request):
   return render(request, 'other_.html')   


def ch_course(request):
   return render(request, 'ch_course.html')   


def csc_course(request):
   return render(request, 'csc_course.html')      

def math_course(request):
   return render(request, 'math_course.html')      


def li_course(request):
   return render(request, 'li_course.html')      


def en_course(request):
   return render(request, 'en_course.html')  

def others(request):
   return render(request, 'others.html')    



def CC(request):
   return render(request, 'CC.html')   


def b_course(request):
   return render(request, 'b_course.html') 

def english_(request):
   return render(request, 'english_.html')   


def computerscience_(request):
   return render(request, 'computerscience_.html')   




def library_(request):
   return render(request, 'library_.html')  



def mathematics_(request):
   return render(request, 'mathematics_.html')      


def biology_(request):
   return render(request, 'biology_.html')




def about(request):
    return render(request, 'about.html')

def handlelogin(request):
    if request.method=="POST":
        #firstname=request.POST.get("pass2")
        #lastname=request.POST.get("lname")
        uname=request.POST.get("uname")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            
            return redirect('/index2')
        else:
            messages.error(request,"INCORRECT USERNAME AND PASSWORD")
            return redirect('/register')

    return render(request, 'register.html')


def handlesignup(request):
    if request.method=="POST":
        #firstname=request.POST.get("pass2")
        #lastname=request.POST.get("lname")
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        
        #print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
            messages.warning(request, "Password Does not Match")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=uname):
               messages.info(request, "Username Already Exists")
               return redirect('/signup')
        except:
            pass     

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email Already Exists")
                return redirect('/signup')
        except:
            pass     



        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request, "Signup Successful")
        return redirect('/register')

    
    return render(request, 'signup.html')


def handlelogout(request):
   logout(request)
   messages.info(request, "Logout Successful")
   return redirect('/register')

   


   


