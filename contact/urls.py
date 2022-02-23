from django.urls import path
from . import views

# URL endpoint for contact form
urlpatterns = [
    path('', views.contact, name='contact'),
]
