from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')  # ✅ after signup, redirect to login page
        else:
            return render(request, 'accounts/signup.html', {'error': 'All fields are required.'})

    # ✅ if GET request → show signup form
    return render(request, 'accounts/signup.html')




from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')  # 👈 change 'home' to your main dashboard or landing page
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


def home_view(request):
    return render(request, 'accounts/home.html')