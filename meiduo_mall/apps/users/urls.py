from django.conf.urls import url

# from .views import RegisterView
from django.urls import reverse

from . import views

urlpatterns = [
  #reverse(users:register) == '/register/'  # 用户注册:
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]