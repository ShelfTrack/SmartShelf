from django.contrib import admin
from django.urls import path, include
from core.views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]