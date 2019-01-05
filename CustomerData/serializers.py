#Customers Data Serializer

#Django
from .models import Customer
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'first_Name', 
            'last_Name', 
            'streetAdd', 
            'city',
            'state',
            'zipNumber'
        )