from django.urls import path
from . import views

urlpatterns = [
    path('cars', views.get_cars),
    path('cars/create', views.create_car),
    path('cars/create', views.create_car),
    path('cars/<int:car_id>', views.update_or_delete_car),
]
