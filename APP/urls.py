from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='APP-home'),
    path('create-post/', views.create_post, name="create-post"),
]