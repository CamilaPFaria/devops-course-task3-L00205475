from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class PetViewTest(APITestCase):
    def test_response_is_correct(self):
        url = reverse('api:pets') #you give it a name and it gives you the url back
        response = self.client.get(url, format='json') #get the response in json format to check if it is sucessfull or other errors codes.
        assert response.status_code == status.HTTP_200_OK #test if it is returning the page - 200 sucess
        body = response.json()
        assert body['message'] == 'Welcome to the Pet API!'


class HealthViewTest(APITestCase):
    def test_response_is_correct(self):
        url = reverse('api:health') #you give it a name and it gives you the url back
        response = self.client.get(url, format='json') #get the response in json format to check if it is sucessfull or other errors codes.
        assert response.status_code == status.HTTP_200_OK #test if it is returning the page - 200 sucess
        body = response.json()
        assert body['status'] == 'okay'        
