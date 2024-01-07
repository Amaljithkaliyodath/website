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
    context={}

    obj=Packages.objects.all()
    context['obj']=obj
    return render(request,'package.html',context)


def blog(request):
    return render(request,'blog.html')

def subpackage(request,id):
    context={}

    obj=Packages.objects.all()
    plan=Subpackage.objects.filter(package=id)
    context['plan']=plan
    context['obj']=obj
    return render(request,'subpackage.html',context)

def gallery(request):
    context={}
    obj=Gallery.objects.all()
    context['obj']=obj
    return render(request,'gallery.html',context)

def branches(request):
    return render(request,'branches.html')

def appointment(request):
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          message=request.POST.get('message')
          age=request.POST.get('age')
          gender=request.POST.get('gender')
          address=request.POST.get('address')
          date=request.POST.get('date')
          time=request.POST.get('time')


          if request.POST:
               details=Appointment.objects.create(name=name,email=email,phone=phone,message=message,age=age,gender=gender,address=address,date=date,time=time)
               details.save()
               return redirect('appointment')
    return render(request,'appointment.html')




def department(request):
    return render(request,'department.html')

def testimoinal(request):
    return render(request,'testimoinal.html')

def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

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
  