import json

from models.MemoryMdl import MemoryMdl
from pattern.MemoryEncoder import MemoryEncoder


class MemoryCtrl:

    def __init__(self):
        pass

    def getRamInfo(self,num):
        mem_mdl = MemoryMdl()
        memory_datas = mem_mdl.get_data(num)
        return json.dumps(memory_datas, cls=MemoryEncoder)
