from celery import Celery

app = Celery('app',include=('app.tasks',))

app.conf.beat_schedule = {
    'add': {
        'task': 'app.tasks.add',
        'schedule': 5,
        'args': (5, 6)
    },
}
