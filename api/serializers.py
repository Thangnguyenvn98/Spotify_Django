from rest_framework import serializers
#Take model Room, and translate to JSON response object
from .models import Room
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields =('id','code','host','guest_can_pause','votes_to_skip','created_at') #Match what you have in room model

