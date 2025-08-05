from django.shortcuts import render
from .decorators import roles_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

@roles_required('admin')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
