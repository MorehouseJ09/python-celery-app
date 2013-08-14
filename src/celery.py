from celery import Celery

celery = Celery("celeryTasks",
		broker="amqp://guest@localhost//",
		backend="amqp://guest@localhost//",
		include=[])

celery.conf.update(CELERY_TASK_RESULT_EXPIRES=3600)

if __name__ == "__main__":

	celery.start()


