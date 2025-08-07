from django.shortcuts import render, redirect
from .decorators import roles_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, LoginForm, EditProfileForm
from django.http import HttpResponseForbidden
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

@roles_required('admin', 'superuser')
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
                if user.is_superuser:
                    return redirect('/admin/')
                elif user.role == 'admin':
                    if user.is_superuser:
                        return redirect('/admin/')
                    else:
                        return redirect('admin_dashboard')
                else:
                    return redirect('home')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# profile_view
@login_required
def profile_view(request, username):
    if request.user.username != username:
        return HttpResponseForbidden("You are not authorized to view this page!")
    return render(request, 'profile.html', {'user': request.user})
    
          
        
# logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


# profile edit view
@login_required
def profile_edit_view(request, username):
    if request.user.username != username:
        return HttpResponseForbidden("You are not authorized to view this page!")
    
    user = request.user
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_view', username=user.username)
    else:
        form = EditProfileForm(instance=user)
    
    return render(request, 'edit_profile.html', {'form': form})
    
