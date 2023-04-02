#store api local to this app

from django.urls import path
from .views import RoomView
#main url wil be run, and adding path here
urlpatterns = [
   
    path('',RoomView.as_view()) 
    
    #function main is called in views where the website look like
                    #Create multiple pat where it would route to the same place, by doing path('/home',main) for instance
]
