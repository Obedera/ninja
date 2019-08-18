from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('console', views.console),
    path('chat', views.chat),
    path('sobre', views.sobre)
]