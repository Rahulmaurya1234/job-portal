# Create your views here.
import email
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CustomUserRegistrationForm

CustomUser = get_user_model()
def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username_or_email, password=password)
        if not user:
            # Try to authenticate with email
            try:
                user_obj = CustomUser.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except CustomUser.DoesNotExist:
                user = None
        if user:
            login(request, user)
            return redirect('home')  # home view banani hogi
        else:
            messages.error(request, "Invalid username/email or password.")
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/register.html')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'accounts/register.html')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'accounts/register.html')

        # Create and save user
        user = CustomUser.objects.create_user(username=username, email=email, password=password, user_type=user_type)
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'accounts/register.html')


