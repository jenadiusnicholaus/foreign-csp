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


def supplier(request):
    context = {

    }
    return render(request, template_name="supplier.html")


def Car(request):
    context = {

    }
    return render(request, template_name="cars.html")
