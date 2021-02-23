from django.urls import path

from .views import (
    MiddagListView,
    MiddagDeleteView,
    MiddagUpdateView,
    MiddagCreateView,
    MiddagDetailView,
)

urlpatterns = [
    path('', MiddagListView.as_view(), name='APP-home'),
    path('middag/<int:pk>/', MiddagDetailView.as_view(), name='middag-detail'),
    path('middag/new/', MiddagCreateView.as_view(), name='middag-create'),
    path('middag/<int:pk>/update', MiddagUpdateView.as_view(), name='middag-update'),
    path('middag/<int:pk>/delete', MiddagDeleteView.as_view(), name='middag-delete'),
]