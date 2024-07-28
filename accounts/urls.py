from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
