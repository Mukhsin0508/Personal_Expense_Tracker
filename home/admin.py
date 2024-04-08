from django.contrib import admin
from .models import Addmoney_info
from django.contrib import admin 
from django.contrib.sessions.models import Session
from .models import UserProfile

# Register your models here.
# Code Explanation:
 # Addmoney_info, UserProfile are the names of the models that we want to register in the database. 
 # list_display contains the name of the columns that will be displayed in the database.

class Addmoney_infoAdmin(admin.ModelAdmin):

    list_display = ("user", "amount", "date", "category", "add_money")

admin.site.register(Addmoney_info, Addmoney_infoAdmin)

admin.site.register(Session)

admin.site.register(UserProfile)
