from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('app_welcome.urls')),
    path('about/', include('app_about.urls')),
    path('representation/', include('app_representation.urls')),
]
