from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("this is my homepage(/)")
    return render(request,"home.html")

def about(request):
    # return HttpResponse("this is my aboutpage(/about)")
    return render(request,"about.html")

def projects(request):
    # return HttpResponse("this is my projectspage(/projects)")
    return render(request,"projects.html")
def contact(request):
    if request.method=="POST":
        name =request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        ins=Contact( name=name , email=email, phone=phone, desc=desc)
        ins.save()
        
    # return HttpResponse("this is my contactpage(/contact)")
    return render(request,"contact.html")

def python(request):
    return render(request,"python.html")

def datascience(request):
    return render(request,"datascience.html")

def rf(request):
    return render(request,"rf.html")
    
    

