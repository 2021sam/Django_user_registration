# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm
from .models import CustomUser


from django.shortcuts import render

# Home view
def home(request):
    return render(request, 'user/home.html')




from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm
from .models import CustomUser

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            messages.success(request, 'You have successfully signed up.')
            return redirect('home')  # Redirect to the home page or another view
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'user/register.html', {'form': form})
