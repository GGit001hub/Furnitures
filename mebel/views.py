from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MebelSerializer,SavatSerializer
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from pprint import pprint

# Create your views here.



class AllView(viewsets.ModelViewSet):
    queryset = Mebel.objects.filter(status="active")
    serializer_class = MebelSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            new_category = Mebel.objects.create(
                name = data['name'],
                addres = data['addres'],
                photo = data['photo'],
                narx = data['narx'],
                chegirma = data['chegirma'],
                like = data['like'],
                razmer = data['razmer'],
                body = data['body'],
                turi = data['turi'],
                rangi = data['rangi'],

            )
            new_category.save()
            serializer = MebelSerializer(new_category)
            return Response(serializer.data)
            # return Response({'succses':"Ma'lumot muvafaqiyatli qo'shildi"})
        except ZeroDivisionError:
            return Response({'error':"Ma'lumot qo'shishda xatolik yuzaga keldi !!!"})

    def update(self, request, *args, **kwargs):
        data = request.data
        mebel = self.get_object()

        try:
            mebel.name = data['name'] if 'name' in data else mebel.name
            mebel.addres = data['addres'] if 'addres' in data else mebel.addres
            mebel.narx = data['narx'] if 'narx' in data else mebel.narx
            mebel.chegirma = data['chegirma'] if 'chegirma' in data else mebel.chegirma
            mebel.like = data['like'] if 'like' in data else mebel.like
            mebel.razmer = data['razmer'] if 'razmer' in data else mebel.razmer
            mebel.turi = data['turi'] if 'turi' in data else mebel.turi
            mebel.body = data['body'] if 'body' in data else mebel.body
            mebel.status = data['status'] if 'status' in data else mebel.status
            mebel.photo = data['photo'] if 'photo' in data else mebel.photo


            mebel.save()
            serializer = MebelSerializer(mebel)
            return Response(serializer.data)

        except:
            return Response({'error':'xatolik'})
    
    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'succses':"O'chirildi"})



class SavatView(viewsets.ModelViewSet):
    queryset = Savat.objects.all()
    serializer_class = SavatSerializer
    permission_classes = [AllowAny]
    
    # def create(self, request, *args, **kwargs):
    #     print('< - - - - - - - - - - - - - - - - - - - - - - - - - - - >')
    #     data = request.data
    #     pprint(data)

    #     # < ---- Foriegn key uchun ---- >
    #     product = False
    #     if 'product' in data:
    #         # try:
    #             product = Savat.objects.get(id=data['product'])
    #             print(product + "--------------------------------- >")
    #         # except:
    #             return Response({'errors':"Bunday malumot mavjut emas"})
    #     # < ---- Foriegn key uchun ---- >


    #     # <--- Takrorlanmasligi uchun --- >
    #     category = Savat.objects.filter(status='active')
    #     for ctg in category:
    #         if ctg.product == data['product']:
    #             return Response({'error':"Bunday kategoriya mavjut. boshqa kiriting !!"})
    #     # <--- Takrorlanmasligi uchun --- >
                
    #     # try:
    #     if product:
    #         print('< - - - - - - - - - - - - - - - - - >')
    #         print(product)
    #         pprint(f"{product} --- > PRODUCT")
    #         new_savat = Savat.objects.create(
    #             product = product,
    #             miqdori = data['miqdori'],
    #             summa = data['summa'],
    #         )
    #     else:
    #         new_savat = Savat.objects.create(
    #             miqdori = data['miqdori'],
    #             summa = data['summa'],
    #         )
    #     print('< - - - - - - - - - - - - - - - - - >')
    #     new_savat.save()
    #     pprint(new_savat)
    #     serizlizer = SavatSerializer(new_savat)
    #     return Response(serizlizer.data)
        # except Exception as e:
            # return Response({'errors':"Malumot to'liq emas"})


