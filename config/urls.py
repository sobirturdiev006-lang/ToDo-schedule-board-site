from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    path('accounts/', include('allauth.urls')),
    path('', lambda request: redirect('account_login')),
]
