#File where the URLS will be defined for the API endpoints
from django.urls import re_path
from .views import pet_view, health_view

app_name = 'api'

urlpatterns = [
    re_path(
        r"^$", health_view, name='health'
    ),
    re_path(
        r"^pets/", pet_view, name='pets'
    )
]

