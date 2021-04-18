import json
from django.http import HttpResponse
from django.core.cache import cache
from datetime import datetime
from .tasks import hello_task
from django.db import connection


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


def run_celery_task(request):
    now = datetime.now()    
    hello_task.delay(data=now)
    response_data ={
        "message": "OK"
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_postres_info_tables(request):
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        for table in cursor.fetchall():
          print(table)
          data.append(table)
    return HttpResponse(json.dumps(data), content_type="application/json")


def health(request):
    return HttpResponse(json.dumps({'status': 'OK'}}), content_type="application/json")
  
