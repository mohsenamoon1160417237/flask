import psutil
from celery.utils.log import get_task_logger
from flask_sqlalchemy import SQLAlchemy

from main_app import celery, flask_app
from managements.MemoryMan import MemoryMan

logger = get_task_logger(__name__)


@celery.task()
def save_memory_data():
    print('save_memory_data start')

    ramMan = MemoryMan()

    ramMan.saveRamToDb()


