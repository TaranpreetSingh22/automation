from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.models import CustomUser
from django.urls import reverse

def login_view(request):
    users = CustomUser.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Manually check the user
        try:
            user = CustomUser.objects.get(username=username)
            
            # Check if the password matches (plain text comparison)
            if user.password == password:
                # Check if the user role matches
                if user.role == role:
                    login(request, user)

                    # Redirect based on user role
                    if user.role == 'admin':
                        return redirect(reverse('adminDashboard:admin_page'))
                    elif user.role == 'rg':
                        return redirect(reverse('registrar:registrar_dashboard'))
                    elif user.role == 'hod':
                        return redirect(reverse('hodDashboard:hod_dashboard'))
                    elif user.role == 'vc':
                        return redirect(reverse('viceChancellor:vc_dashboard'))
                    elif user.role == 'finance':
                        return redirect(reverse('financeManagement:finance_dashboard'))
                else:
                    return render(request, 'login.html', {'error': 'Role mismatch!','users': users})
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password','users': users})

        except CustomUser.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html', {'users': users})
