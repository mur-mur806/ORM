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