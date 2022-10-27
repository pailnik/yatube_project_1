from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index),
    path('groups/', views.groups_list, name='groups_list'),
    path('groups/<slug:slug>/',
         views.groups_detail)
    ]