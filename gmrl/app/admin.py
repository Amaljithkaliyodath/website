from django.contrib import admin
from . models import *
# Register your models here.


class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']



admin.site.register(Contact,Contact_display)
