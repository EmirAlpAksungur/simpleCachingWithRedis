from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

# For cache timeout
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class TestView(APIView):
    def get(self, request):

        # Locate name in redis database
        if 'name' in cache:
            # get results from cache
            name = cache.get('name')
            # cache.clear()
            print('form cache')
            return Response(name)

        # If not found 
        else:
            result = {
                "name": "form cache"
            }

            # store data in cache
            cache.set('name', result, timeout=CACHE_TTL)

            print('not from cache')
            return Response(result)