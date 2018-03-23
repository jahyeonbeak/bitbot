from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_done

"""bitbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from arbitrage import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(r'', views.index, name='indexpage'),
    #path(r'index/', views.Login.as_view(), name='indexpage'),
    #path(r'main/', views.MainPage.as_view(), name='mainpage'),
    url(r'', include('arbitrage.urls')),
    #url(r'^$', views.dashboard, name='dashboard'),
    #url(r'^register/$', views.register, name='register'),

]