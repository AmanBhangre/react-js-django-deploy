from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogApi.as_view())
]
