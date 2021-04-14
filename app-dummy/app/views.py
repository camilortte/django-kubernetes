import json
from django.http import HttpResponse
from django.core.cache import cache

KEY = 'caca'

def create_in_redis(request):
    data = request.GET.get('data')
    if data:        
        response_data ={
            "message": "OK"
        }
        cache.set(KEY, data)
    else:
        response_data ={
            "message": "Fail"
        }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_from_redis(request):
    response_data ={
        "message": "OK",
        "data": cache.get(KEY)
    }    
    return HttpResponse(json.dumps(response_data), content_type="application/json")