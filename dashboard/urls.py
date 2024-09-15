from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.product_delete, name='dashboard-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail, name='dashboard-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit, name='dashboard-products-edit'),
    path('staff/', views.staff, name='dashboard-customers'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('order/', views.order, name='dashboard-order'),
]
