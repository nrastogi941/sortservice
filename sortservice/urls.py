from django.urls import path
from .views import SortServiceView

urlpatterns = [
    path('sort-search/', SortServiceView.as_view(), name='sort-search'),
]