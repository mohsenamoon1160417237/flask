import json

from models.memory_mdl import MemoryMdl
from pattern.memory_encoder import MemoryEncoder


class MemoryCtrl:

    @classmethod
    def get_ram_info(cls, num):
        mem_mdl = MemoryMdl()
        memory_datas = mem_mdl.get_data(num)
        return json.dumps(memory_datas, cls=MemoryEncoder)
