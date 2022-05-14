from django.contrib.auth import views as auth_views
from django.urls import path

from admin_panel import views

app_name="admin_panel"

urlpatterns = [
    path('', views.index, name="index"),
    path('account/', views.account, name="account"),

    path("clients/", views.ClientView.as_view(), name="clients"),
    path("deleteclient/<str:cnic>/", views.ClientViewDelete.as_view(), name="deleteClient"),
    path("updateclient/<str:cnic>", views.updateClient, name="updateClient"),

    path("property/", views.PropertyView.as_view(), name="property"),
    path("deleteproperty/<str:plot>/", views.PropertyViewDelete.as_view(), name="deleteProperty"),
    path("updateproperty/<str:plot>", views.updateProperty, name="updateProperty"),

    path("file/", views.FileView.as_view(), name="file"),
    path("deletefile/<str:file>/", views.FileViewDelete.as_view(), name="deleteFile"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
