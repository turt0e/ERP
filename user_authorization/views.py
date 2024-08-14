from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard:index')
    else:
        form = AuthenticationForm()
    return render(request, 'user_authorization/signin.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('user_authorization:signin')
