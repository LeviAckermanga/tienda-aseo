from django.shortcuts import render

def home(request):
    return render(request, 'productos/home.html')

def productos(request):
    return render(request, 'productos/home.html')

def carrito(request):
    return render(request, 'productos/carrito.html')

def contacto(request):
    return render(request, 'productos/contacto.html')
