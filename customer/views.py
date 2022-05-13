from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/index.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/about.html")

def agent(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/agent-single.html")

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/contact.html")

def property(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/property-grid.html")

def property_single(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/property-single.html")

def sign_in(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/sign-in.html")

def sign_up(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/sign-up.html")






