# make sure that we have absolute imports enabled to ensure that we import the correct modules
#http://www.python.org/dev/peps/pep-0328/
from __future__ import absolute_import

# initialize celery imports as needed
from celery import Celery

# now initialize celery global object
# backend is the results backend to store results
celery = Celery("src.celery",
		broker="amqp://guest@localhost",
		backend="amqp://guest@localhost",
		include=["src.tasks"])

# now configure other celery configuration element
celery.conf.update(CELERY_TASK_RESULT_EXPIRES=3600,)

# if this is being called from the main module, go ahead and start up celery
if __name__ == "__main__":

	celery.start()


