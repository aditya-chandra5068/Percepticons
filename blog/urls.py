from django.urls import path
from . import views

# URL endpoints for the blog page
urlpatterns = [
        path('',views.blogHome, name='blogHome'),
        path('<str:slug>',views.blogPost, name='blogPost'),
        path('<str:slug>/edit',views.editPost, name='editPost'),
]
