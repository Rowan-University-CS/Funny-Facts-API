from rest_framework.response import Response
from rest_framework.decorators import api_view

# TODO - Add additional API endpoints (see README file for details)
@api_view(['GET'])
def get_test(request):
    fact = {'fact': 'butterflies smell with their feet.'}
    return Response(fact)