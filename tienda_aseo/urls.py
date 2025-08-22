from django.contrib import admin
from django.urls import path, include
from productos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('carrito/', views.carrito, name='carrito'),
    path('contacto/', views.contacto, name='contacto'),
]