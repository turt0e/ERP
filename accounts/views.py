from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        password_confirm = form.cleaned_data.get('password_confirm')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'accounts/register.html', context)