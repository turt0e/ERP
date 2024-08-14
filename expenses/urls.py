from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.expenses_dashboard, name='dashboard'),
]
