from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='lista_productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('contacto/', views.contacto, name='contacto'),
]
