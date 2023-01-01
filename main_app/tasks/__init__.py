from celery.utils.log import get_task_logger

from main_app import celery
from managements.memory_man import MemoryMan

logger = get_task_logger(__name__)


@celery.task()
def save_memory_data():
    ram_man = MemoryMan()
    ram_man.save_ram_to_db()
