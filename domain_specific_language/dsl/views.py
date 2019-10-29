from rest_framework.decorators import api_view
from.serializers import *


@api_view(['POST'])
def dsl_view(request):
	
	data = request.data
	serializer = DslSerializer(data)
	return Response(serializer.create_sql_query())
