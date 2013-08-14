from celery import Celery
from tasks import add

celery = Celery('tasks', broker='amqp://guest@localhost')

@celery.task
def add(x,y):
	
	return x + y


add.delay(4, 4)




