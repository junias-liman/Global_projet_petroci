"""
URL configuration for Global_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Global_project.views import home_general,entete
from Station_Essence.views import login_user

urlpatterns = [
        path('Station/', include('Station_Essence.urls')),
     path('admin/', admin.site.urls),
    path('accueil/',home_general),
    path('',entete,name='tete'),
    path('accounts/login/',login_user,name="login")
]
