from django.shortcuts import render
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

import json

# Create your views here.
@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):

    if request.method == 'GET':
        instance = Product.objects.all().order_by('?').first()
        if instance:
            model_data = ProductSerializer(instance=instance).data

        return Response(data=model_data) 

    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            print(instance)
            return Response(serializer.data)

    return Response({"invalid": "bad data"}, status=400)
