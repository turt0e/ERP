from django.shortcuts import redirect

def redirect_to_signup(request):
    return redirect('user_authorization:signup')
