from . import views
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-dash/', views.admin_dashboard, name='admin_dashboard'),
]