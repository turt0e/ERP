from django.urls import path
from . import views

app_name = 'user_authorization'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
