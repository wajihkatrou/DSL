from rest_framework import serializers
from cities.serializers import *


class DslSerializer(serializers.Serializer):
		
	fields = serializers.ListField(child=serializers.CharField())
	filters = serializers.JSONField(required=False)

	def create_sql_query(self):
		citySerializer = CitySerializer()
		valide_keys = list(citySerializer.fields.keys())
		
		sql_query = "SELECT "
		
		query = self.data

		for field in query["fields"]:
			if field in valide_keys:
				sql_query += field + ", "
			else:	
				return f"The key {field} is not in table schema! Please enter a valid JSON"
		
		sql_query = sql_query[:-2] + " FROM city;"

		return sql_query