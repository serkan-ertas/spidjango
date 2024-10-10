from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='spider-home'),
    path('about/', views.about, name='spider-about'),
    path('<str:spider_name>/', views.spider, name='run_spider'),
]