from .views import RegistrationView
from django.urls import path

urlpatterns = [
    path('kayit/', RegistrationView.as_view(), name='kayit_ol'),
]