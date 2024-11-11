from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        remember_me = 'remember_me' in request.POST

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Check role if applicable (This part can be customized as needed)
            if role == 'admin' and user.is_staff or role == 'user' and not user.is_staff:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks for remember me
                return redirect('home')  # Redirect to a homepage or dashboard
            else:
                messages.error(request, "Role mismatch.")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'accounts/login.html')
