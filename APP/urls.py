from django.urls import path
from . import views
from .views import (
    MiddagListView

)

urlpatterns = [
    path('home/', MiddagListView.as_view(), name='APP-home'),
]