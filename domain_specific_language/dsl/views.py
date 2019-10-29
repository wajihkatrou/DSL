from rest_framework.decorators import api_view
from.serializers import *
from rest_framework.response import Response


@api_view(['POST'])
def dsl_view(request):
	
	data = request.data
	serializer = DslSerializer(data)
	return Response(serializer.create_sql_query())
