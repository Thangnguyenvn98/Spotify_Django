from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    #return a response
    return HttpResponse("<h1>My Man</h1>")
