from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def java(request):
    return render(request,'java.html')
def javaadv(request):
    return HttpResponse('<h1>JAVA IS CURRENTLY ONE OF THE TRENDING LANGUAGE</h1>')
