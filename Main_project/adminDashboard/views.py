from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def admin_page(request):
    users = User.objects.all()
    return render(request, 'adminDashboard/admin_page.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = UserForm()
    return render(request, 'adminDashboard/add_user.html', {'form': form})
