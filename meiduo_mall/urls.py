"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

from meiduo_mall.apps.users import views

urlpatterns = [
    path('admin/', admin.site.urls),
   # re_path(r'^', include('users.urls', namespace='users')),
  #  path('register/', include('users.urls')),
    path('', include("users.urls")),
    re_path(r'^$',views.RegisterView.as_view(), name='register'),#输入Ip地址自动跳转到首页

]
