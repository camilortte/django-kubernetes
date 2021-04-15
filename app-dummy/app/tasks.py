from celery import Celery
from django.core.cache import cache

from celery import shared_task

@shared_task
def hello_task(data):
    print(f'Request: {data}')
    cache.set('caca', data)

