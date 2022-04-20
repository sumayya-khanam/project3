from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import numbers

class numbersSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = numbers
        fields = '__all__'