from django.shortcuts import  render,redirect
from . models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def test(request):
    return render(request,'test.html')

def package(request):
    return render(request,'Package.html')
def blog(request):
    return render(request,'blog.html')

def gallery(request):
    return render(request,'gallery.html')

def branches(request):
    return render(request,'branches.html')

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        if request.POST:
            details=contactus.objects.create(name=name,email=email,phone=phone,message=message,subject=subject)
            details.save()
            return  redirect('contactus')
    return render(request,'contactus.html')
  