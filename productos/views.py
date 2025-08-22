from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()[:6]  # Mostrar 6 productos destacados
    return render(request, "home.html", {"productos": productos})
