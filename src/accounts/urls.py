from django.urls import path, include

from .views import Register
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]
