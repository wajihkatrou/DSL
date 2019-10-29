from rest_framework import viewsets
from .models import *
from .serializers import *


class CityViewSet(viewsets.ModelViewSet):
	
	queryset = City.objects.all()
	serializer_class = CitySerializer