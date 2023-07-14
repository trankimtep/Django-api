from django.urls import path
from . import views

urlpatterns = [
    path('cars', views.get_cars),
    path('cars/create', views.create_car),
]
