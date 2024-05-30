from django.urls import path
from .views import property_list_create, property_detail, property_update, property_delete

urlpatterns = [
    path('properties/', property_list_create, name="property_list_create"),
    path('properties/<int:pk>/', property_detail, name="property_detail"),
    path('properties/<int:pk>/edit/', property_update, name="property_update"),
    path('properties/<int:pk>/delete/', property_delete, name="property_delete"),
]
