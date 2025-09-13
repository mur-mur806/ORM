# Ex02 Django ORM Web Application
## Date: 13/10/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
models.py```
from django.db import models
from django.contrib import admin
class Car_DB (models.Model):
     Cars_Name=models.CharField(max_length =15)
     Carsno=models.IntegerField(primary_key=True)
     price=models.IntegerField()
     model=models.CharField()
     version=models.FloatField()
class Car_DBAdmin (admin.ModelAdmin):
     list_display = ["Cars_Name","Carsno","price","model","version"]

admin.py
from django.contrib import admin
from .models import Car_DB, Car_DBAdmin
admin.site.register(Car_DB, Car_DBAdmin)

```



## OUTPUT

Include the screenshot of your admin page.

Screenshot (14).png   
## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
