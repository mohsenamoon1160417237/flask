import psutil
from models.MemoryMdl import MemoryMdl


class MemoryMan:

    def __init__(self):
        pass

    @staticmethod
    def __get_ram_inf():
        total = psutil.virtual_memory().total / 1000000
        used = psutil.virtual_memory().used / 1000000
        free = psutil.virtual_memory().free / 1000000

        return total, used, free

    def save_ram_to_db(self):
        total, used, free = self.__get_ram_inf()
        memory_data = MemoryMdl(total=total, free=free, used=used)
        memory_data.save_to_db()
