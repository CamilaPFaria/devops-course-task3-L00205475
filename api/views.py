from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet
from .serializers import PetSerializer

# Endpoints of the API


class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
            "status": "okay"
            }   
        )
        
health_view = HealthView.as_view() #instantiate the view and assign it to a variable

#List all pets and/or create new pets
class PetView(APIView):
    def get(self, request, *args, **kwargs):
        all_pets = Pet.objects.all()
        serializer = PetSerializer(all_pets, many=True)
        return Response(serializer.data)

    def post(self, request,*args,**kwargs):
        data = request.data #receives the JSON sent by curl

        serializer = PetSerializer(data=data) #passed the icnomig data to the serializer
        serializer.is_valid(raise_exception=True) #Checks if the data satisfies the model and serializer validation rules.
        serializer.save() #Creates and saves Pet in the database.
    
        return Response(serializer.data) #Returns the newly created Pet as serialized data.
        
        
pet_view = PetView.as_view() #instantiate the view and assign it to a variable