from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView, RedirectView

from admin_panel.models import Agent
from admin_panel.forms import AgentForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "customer/index.html")

class About(TemplateView):
    template_name = "customer/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['agents'] = Agent.objects.all()
        return context

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







