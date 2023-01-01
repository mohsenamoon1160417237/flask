import json

from models.MemoryMdl import MemoryMdl
from patterns.MemoryEncoder import MemoryEncoder


class MemoryCtrl:

    def get_ram_info(self,num):
        mem_mdl = MemoryMdl()
        memory_datas = mem_mdl.get_data(num)
        return json.dumps(memory_datas, cls=MemoryEncoder)
