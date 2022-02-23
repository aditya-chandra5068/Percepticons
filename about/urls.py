from django.urls import path
from . import views

# URL endpoint for about page after which about page will be rendered
urlpatterns = [
    path('', views.about, name='about'),
]
