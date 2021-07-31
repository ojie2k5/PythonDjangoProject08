from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm is
# unused since we are using UserRegisterForm from user/forms.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You account has been created! You are now able to login {username}!')
            # Below redirect users after successfully created a profile
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# a user must be log in to view this page
@login_required
def profile(request):
    return render(request, 'users/profile.html')