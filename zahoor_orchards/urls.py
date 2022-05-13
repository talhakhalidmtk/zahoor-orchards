from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('admin-no/', admin.site.urls),
    path('', include('customer.urls')),
    path('admin/', include('admin_panel.urls')),
]
