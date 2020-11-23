from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('courage.urls')),
    path(r'admin/', admin.site.urls),
]
