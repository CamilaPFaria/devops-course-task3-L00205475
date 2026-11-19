from django.db import models

#Ref.: https://docs.djangoproject.com/en/5.2/topics/db/models/
class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


