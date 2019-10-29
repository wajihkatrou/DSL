from rest_framework import serializers
from cities.serializers import *
import json

class DslSerializer(serializers.Serializer):
		
	fields = serializers.ListField(child=serializers.CharField())
	filters = serializers.JSONField(required=False)


	def create_sql_query(self):
		#Get the valid fields in the table schema
		citySerializer = CitySerializer()
		valide_keys = list(citySerializer.fields.keys())
		
		#Dictionnary to use when we transform predicate filters
		replace_with = {"eq" : "=", "gt" : ">", "lt" : "<", "contains" : "in"}
		
		sql_query = "SELECT "
		
		query = self.data
		
		for field in query["fields"]:
			if field in valide_keys:
				sql_query += field + ", "
			else:	
				return f"The key {field} is not in table schema! Please enter a valid JSON"
		
		sql_query = sql_query[:-2] + " FROM city"

		if "filters" in query:
			filters = query["filters"]
			if filters['field'] not in valide_keys:
				return f"The filter field {filters['field']} is not in table schema!"
			if "predicate" in filters:
				replace = filters['predicate'].replace(filters['predicate'], replace_with[filters['predicate']])
				sql_query += f" WHERE {filters['field']} {replace} {filters['value']}"
			else:
				sql_query += f" WHERE {filters['field']} {replace_with['eq']} {filters['value']}"
		
		return sql_query + ";"