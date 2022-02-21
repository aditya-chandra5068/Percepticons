from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/<int:topic_id>/',views.topic, name='topic'),
    path('search',views.search, name='search'),
]
