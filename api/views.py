from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room   #Create a class and inherit from generics
# Create your views here.


class RoomView(generics.ListAPIView):  #Make this CreateAPIVIew, ListAPIVIEW
    queryset = Room.objects.all()
    serializer_class = RoomSerializer



