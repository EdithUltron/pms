"""Interactive_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home.views import highereducationaction, home, placementaction, profileaction
from login.views import loginaction
from signup.views import signaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginaction,name="login"),
    path('signup/',signaction,name="signup"),
    path('',home,name="home"),
    path('profile/',profileaction,name="profile"),
    path('placement/',placementaction,name="placement"),
    path('highereducation/',highereducationaction,name="highereducation"),
]
