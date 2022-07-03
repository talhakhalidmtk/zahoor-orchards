from django.contrib.auth import views as auth_views
from django.urls import path

from customer import views

app_name="customer"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.About.as_view(), name="about"),
    path('agent/', views.agent, name="agent"),
    path('contact/', views.contact, name="contact"),
    path('property/', views.property, name="property"),
    path('property-single/', views.property_single, name="property-single"),
]
