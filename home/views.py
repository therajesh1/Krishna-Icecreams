from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact,Sign
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate


# Create your views here.




def sign(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        # sign=Sign(email=email,password=password,date=datetime.today())
        user=authenticate(email=email,password=password)
        if user is not None:
            return redirect("/sign.html")
            messages.success(request, "password or email is incorrect")
        else:
            return render(request,'dashboard.html')
        # sign.save()
        # messages.success(request, "you have successfully signed in!")
    return render(request,'sign.html')

def index(request):
    context={
        'variable1':"this is sent",#calling a variable
        'variable2':"this is recieved"
    }
    # if request.user.is_anonymous:
    #     return redirect ("/sign.html")
    return render(request,'index.html',context)

    # return HttpResponse("this is homepage")
    


def dashboard(request):
    return render(request,'dashboard.html')


def about(request):
    return render(request,'about.html')
    

def services(request):
    return render(request,'services.html')
    

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('msg')
        contact=Contact(name=name,email=email,phone=phone,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent")

    return render(request,'contact.html')


            
         

        
       
    

    
def logout(request):
    logout()
    return render(request,'proceed.html')