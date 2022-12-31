import psutil
from celery.utils.log import get_task_logger

from memory_data import celery
from memory_data.main import MemoryData, db

logger = get_task_logger(__name__)


@celery.task()
def save_memory_data():
    total = psutil.virtual_memory().total / 1000000
    used = psutil.virtual_memory().used / 1000000
    free = psutil.virtual_memory().free / 1000000

    memory_data = MemoryData(total=total, free=free, used=used)
    db.session.add(memory_data)
    db.session.commit()

    logger.info(f"Saved memory data with free: {free}, used: {used}, total: {total}")
