from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.index, name='posts'),
    path('group_posts/', views.group_posts, name='group_posts'),
]