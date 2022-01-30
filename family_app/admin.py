from django.contrib import admin
from .models import PhotoGallary

@admin.register(PhotoGallary)
class imageadmin(admin.ModelAdmin): 
    list_display=['id','multipleimages'] 
 
