from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def javascript(request):
    return render(request,'javascript.html')
def javascriptadv(request):
    return HttpResponse('<h1>JAVASCRIPT IS MAINLY USED FOR CREATING WEB APPLICATIONS</h1>')
