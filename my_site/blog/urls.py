from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:postname>/', views.post, name='post_detail'),
]
