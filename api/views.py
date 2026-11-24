from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet
from .serializers import PetSerializer
from django.http import HttpResponse
from .metrics import REQUEST_COUNT, PET_COUNT, generate_latest, CONTENT_TYPE_LATEST

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
        REQUEST_COUNT.inc() #increases the request counter by one every time this endpoint is accessed.
        all_pets = Pet.objects.all()
        PET_COUNT.set(all_pets.count())#updates the gauge with the current number of pets in the database.
        serializer = PetSerializer(all_pets, many=True)
        return Response(serializer.data)

    def post(self, request,*args,**kwargs):
        REQUEST_COUNT.inc() #counts the amount of requests to create pets
        data = request.data #receives the JSON sent by curl

        serializer = PetSerializer(data=data) #passed the icnomig data to the serializer
        serializer.is_valid(raise_exception=True) #Checks if the data satisfies the model and serializer validation rules.
        serializer.save() #Creates and saves Pet in the database.
    
        return Response(serializer.data) #Returns the newly created Pet as serialized data.
    
          
        
pet_view = PetView.as_view() #instantiate the view and assign it to a variable

def metrics_view(request):
    return HttpResponse(
        generate_latest(),
        content_type=CONTENT_TYPE_LATEST
    ) 

