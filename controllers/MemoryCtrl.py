import json

from models.MemoryMdl import MemoryMdl
from patterns.MemoryEncoder import MemoryEncoder


class MemoryCtrl:

    @classmethod
    def get_ram_info(cls, num):
        mem_mdl = MemoryMdl()
        memory_datas = mem_mdl.get_data(num)
        return json.dumps(memory_datas, cls=MemoryEncoder)
