from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path('', views.homepage, name='homepage'),
    path('index.html', views.homepage, name='index'),
    path('org_manage.html', views.org_manage, name='org_manage')
]