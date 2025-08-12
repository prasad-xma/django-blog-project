from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='home'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('myblog/', views.my_blog, name='my_blog'),
]
