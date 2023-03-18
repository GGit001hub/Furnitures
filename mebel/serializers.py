from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image',]
        
class MebelSerializer(serializers.ModelSerializer):
    imagine = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Mebel
        fields = ["id","name",'slug',"addres","narx","chegirma","chegirma_narxi","like","razmer","body","turi","rangi","photo","imagine"]



class SavatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = ['id','product','miqdori','summa']
