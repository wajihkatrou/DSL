from rest_framework import serializers
from .models import *

class CitySerializer(serializers.HyperlinkedModelSerializer):

	reg_name = serializers.CharField(source='region.region_name')
	reg_code = serializers.IntegerField(source='region.region_code')

	class Meta:
		model = City
		fields = ('code', 'name', 'population', 'average_age', 'distr_code', 'dept_code', 'reg_code', 'reg_name')
