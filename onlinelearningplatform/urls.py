"""
URL configuration for onlinelearningplatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from .views import index
from .views import canvas
from .views import googleclassroom
from .views import microsoftteams
from .views import moodle
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'index'),
    path('canvas/',canvas,name='canvas'),
    path('googleclassroom/',googleclassroom,name='googleclassroom'),
    path('microsoftteams/',microsoftteams,name='microsofteams'),
    path('moodle/',moodle,name='moodle'),
    path('accounts/', include('accounts.urls')),
    path('forms/', views.forms, name='forms'),
    path('canvas/', include('canvas.urls')),
]