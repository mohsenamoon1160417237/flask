import psutil
from models.MemoryMdl import MemoryMdl


class MemoryMan:

    def __init__(self):
        pass

    def __getRamInf(self):
        total = psutil.virtual_memory().total / 1000000
        used = psutil.virtual_memory().used / 1000000
        free = psutil.virtual_memory().free / 1000000
        print(f"Saved memory data with free: {free}, used: {used}, total: {total}")
        print('save_memory_data got data')
        return total,used,free

    def saveRamToDb(self):
        total,used,free = self.__getRamInf()
        memory_data = MemoryMdl(total=total, free=free, used=used)
        print('memory_data')
        print(memory_data)
        memory_data.saveToDb()

