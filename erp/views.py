from django.shortcuts import redirect
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def redirect_to_signup(request):
    return redirect('user_authorization:signup')
