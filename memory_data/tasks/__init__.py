import psutil
from celery.utils.log import get_task_logger
from flask_sqlalchemy import SQLAlchemy

from memory_data import celery, flask_app
from utility.RamManagement import RamManagement

logger = get_task_logger(__name__)


@celery.task()
def save_memory_data():
    print('save_memory_data start')

    db = SQLAlchemy(flask_app)

    ramMan = RamManagement(db)

    ramMan.saveRamToDb()


