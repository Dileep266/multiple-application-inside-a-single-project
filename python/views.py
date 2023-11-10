from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def python(request):
    return render(request,'python.html')
def pythonadv(request):
    return HttpResponse('<h1>python is mainly used for datascience and machine learning</h1>')