"""
URL configuration for project6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from java.views import *
from python.views import *
from javascript.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('java/',java,name='java'),
    path('javaadv/',javaadv,name='javaadv'),
    path('python/',python,name='python'),
    path('pythonadv/',pythonadv,name='pythonadv'),
    path('javascript/',javascript,name='javascript'),
    path('javascriptadv/',javascriptadv,name='javascriptadv'),

]
