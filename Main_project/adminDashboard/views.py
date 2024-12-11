from django.shortcuts import render, redirect
from login.models import CustomUser
from django.contrib import messages

def admin_page(request):
    users = CustomUser.objects.all()
    return render(request, 'adminDashboard/admin_page.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
        else:
            # Add the user directly to the database
            new_user = CustomUser.objects.create(
                username=username,
                email=email,
                role=role,
                password=password
            )
            messages.success(request, f"User '{new_user.username}' added successfully!")
            return redirect('adminDashboard:admin_page')
    
    return render(request, 'adminDashboard/add_user.html')
