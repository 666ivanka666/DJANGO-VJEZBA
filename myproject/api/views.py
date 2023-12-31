from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item

from .serializers import ItemSErializer

import os
from django.conf import settings

# Manually configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
settings.configure()

from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response

# Now you can define your views and other code here...
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
