from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet

# Endpoints of the API


class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
            "status": "okay"
            }   
        )
        
health_view = HealthView.as_view() #instantiate the view and assign it to a variable


class PetView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
            "message": "Welcome to the Pet API!"
            }   
        )
        
pet_view = PetView.as_view() #instantiate the view and assign it to a variable