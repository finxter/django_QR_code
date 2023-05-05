from django.urls import path
from .views import generate_QR_code


urlpatterns = [
    path('', generate_QR_code, name='home'),
]
