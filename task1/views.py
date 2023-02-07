from django.shortcuts import render
from .models import Food
from .serializers import FoodSerializer
from rest_framework.response import Response
from rest_framework import viewsets,status


class ShowViewSet(viewsets.ModelViewSet):

    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def create(self,request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        search  = data['Product']
        queryset = Food.objects.filter(Product = search ).values()
        print(serializer.data,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        return Response(queryset)    

    def get_queryset(self):
        queryset = Food.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(Product = search)
        return queryset    