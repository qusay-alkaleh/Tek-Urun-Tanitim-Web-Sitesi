from django.urls import path
from sinp_app import views

urlpatterns = [
    path('products/', views.products.as_view(), name='products'),
    path('products/<int:pk>/', views.product_detail.as_view(), name='product_detail'),
]
