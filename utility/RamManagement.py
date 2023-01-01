import psutil

from memory_data.tasks import logger
from utility.db.MemoryData import MemoryData


class RamManagement:


    def __init__(self,db):
        self.db = db

    def getRamInf(self):
        total = psutil.virtual_memory().total / 1000000
        used = psutil.virtual_memory().used / 1000000
        free = psutil.virtual_memory().free / 1000000
        logger.info(f"Saved memory data with free: {free}, used: {used}, total: {total}")
        print('save_memory_data got data')
        return total,used,free

    def saveRamToDb(self):
        total,used,free = self.getRamInf()
        memory_data = MemoryData(db=self.db, total=total, free=free, used=used)
        print('memory_data')
        print(memory_data)
        memory_data.saveToDb()

