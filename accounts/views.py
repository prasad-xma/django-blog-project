from django.shortcuts import render, redirect
from .decorators import roles_required
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, LoginForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

@roles_required('admin')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# register
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            user.role = 'user'
            
            # save user
            user.save()
            
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
    
# login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                # redirect by role
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('home')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    

