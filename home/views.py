from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):

    # peoples=[
    #     {'Name' : 'Ankit', 'Age' : 23 },
    #     {'Name' : 'Rakesh', 'Age' : 18  },
    #     {'Name' : 'Pooja', 'Age' : 24  },
    #     {'Name' : 'Riya', 'Age' : 17  },
    #     {'Name' : 'Akansha', 'Age' : 19  },
    #     {'Name' : 'Rajat', 'Age' :22  },

    # ]
    queryset=Students.objects.all()
    context={
        'data' : queryset
    }
    return render(request,'index.html',context)


def submit_details(request):
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        mobile_no=data.get('number')
        photo=request.FILES.get('photo')
    
        Students_Profile.objects.create(
            name=name,
            email=email,
            phone_number=mobile_no,
            photo=photo,
            )
        messages.success(request," Details Saved in Database!")
        return redirect('/submit-details/')
    
    
    queryset=Students_Profile.objects.all()
        #Adding Search Functionality

    if request.GET.get('search'):
        queryset=queryset.filter(name__icontains=request.GET.get('search'))

    
    
    context={
        'data' : queryset
    }
 
    return render(request,'form.html', context)

def delete_details(request,id):
    
    queryset=Students_Profile.objects.get(id=id)
    queryset.delete()
    return redirect('/submit-details/')
    
def Edit(request,id):
    queryset=Students_Profile.objects.get(id=id)
    context={
        'data':queryset
    }

    if request.method=="POST":
        data=request.POST
        new_name=data.get('name')
        new_no=data.get('number')

        queryset.name=new_name
        queryset.phone_number=new_no
        queryset.save()
        messages.success(request,"Edit User Details!")
        return redirect('/submit-details/')

    return render(request, 'edit.html',context)


def login_page(request):

    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')

        if not User.objects.filter(username=username).exists():

            messages.error(request,"Invalid Credentials")
            return redirect('/login')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/submit-details/')

        else:
            messages.error(request,"Wrong password")
            return redirect('/login')
            

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request,"Already Username Taken")
            return redirect('/register/')

        user=User.objects.create(
             first_name=first_name,
             username=username,
             email=email,
             
        )

        user.set_password(password)  #use for encrypt the password
        user.save()
        subject = 'welcome to techno fitness'
        message = f'Hi {user.username}, thank you for registering in Techno fitness.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list =[user.email, ]
        send_mail( subject, message, email_from, recipient_list) 
        messages.success(request,"Successfully Registered")
        return redirect('/login')
            
            

    return render(request,'register.html')