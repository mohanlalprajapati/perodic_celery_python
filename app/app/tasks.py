from .celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(bind=True)
def add(self, x, y):
    logger.info(f'Adding X and Y: {x} and {y}')
    return x + y
