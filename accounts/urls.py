from . import views
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-dash/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # user profile
    path('profile/<str:username>/', views.profile_view, name='profile')
]