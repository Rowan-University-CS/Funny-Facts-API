from django.urls import path
from . import views

# TODO - add paths for new API endpoints created
urlpatterns = [
    path('', views.get_test),
]