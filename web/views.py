from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import appuser
from .forms import AppUserRegistrationForm, AppUserLoginForm

# Create your views here.
# Create your views here.
def home(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def base(request):
    return render (request, 'base.html')
def error(request, exception=None):
    return render (request, '404.html', status=404)

def appointment(request):
    return render (request, 'appointment.html')

def contact(request):
    return render (request, 'contact.html')

def courses(request):
    return render (request, 'courses.html')

def feature(request):
    return render (request, 'feature.html')

def team(request):
    return render (request, 'team.html')

def testimonial(request):
    return render (request, 'testimonial.html')

def register_user(request):
    if request.method == 'POST':
        form = AppUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Hash the password securely
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = AppUserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AppUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = appuser.objects.get(username=username)
                if check_password(password, user.password):
                    # Password is correct! Set session.
                    request.session['appuser_id'] = user.id
                    request.session['appuser_username'] = user.username
                    return redirect('home')
                else:
                    form.add_error('password', 'Invalid password')
            except appuser.DoesNotExist:
                form.add_error('username', 'User does not exist')
    else:
        form = AppUserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    # Clear session data
    if 'appuser_id' in request.session:
        del request.session['appuser_id']
    if 'appuser_username' in request.session:
        del request.session['appuser_username']
    return redirect('home')
