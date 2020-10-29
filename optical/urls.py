from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path('', views.homepage, name='homepage'),
    path('index.html', views.homepage)
]