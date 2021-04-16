from celery import Celery
from django.core.cache import cache
from datetime import datetime
from celery import shared_task
from time import sleep


@shared_task
def hello_task(data):
    print(f'Request: {data}')
    cache.set('caca', data)


@shared_task
def scheduler():
    now = datetime.now()    
    print(f"Priting shit {now}")
    sleep(10)