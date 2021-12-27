from django.shortcuts import render

# Create your views here.


def home(request):
    context = {

    }
    return render(request, template_name='home.html', context=context)


def login(request):
    context = {

    }
    return render(request, template_name="login.html")


def register(request):
    context = {

    }
    return render(request, template_name="register.html")


def supplierlist(request):
    context = {

    }
    return render(request, template_name="supplier.html")


def add_suppliers(request):
    return render(request, template_name="add_supplier.html")


def cars(request):
    return render(request, template_name="cars.html")


def add_cars(request):
    return render(request, template_name="add_car.html")


def add_cars(request):
    return render(request, template_name="add_car.html")


def customers(request):
    return render(request, template_name="customers.html")
