from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        
class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name
        
class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = ['id', 'title', 'price', 'inventory']