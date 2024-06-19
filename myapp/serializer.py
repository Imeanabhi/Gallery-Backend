from rest_framework import serializers
from myapp.models import Image,UserInterface

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields="__all__"

class UserInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInterface
        fields="__all__"