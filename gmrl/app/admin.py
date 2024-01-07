from django.contrib import admin
from . models import *
# Register your models here.


class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']


class Gallery_display(admin.ModelAdmin):
    list_display=['image']


class Packages_display(admin.ModelAdmin):
    list_display=['image','description']


class Appointment_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','date','time','address','gender','age']

class Subpackage_display(admin.ModelAdmin):
    list_display=['image','t1','t2','t3','t4','t5','name','cost']    

admin.site.register(Contact,Contact_display)
admin.site.register(Appointment,Appointment_display)
admin.site.register(Gallery,Gallery_display)
admin.site.register(Packages,Packages_display)
admin.site.register(Subpackage,Subpackage_display)
