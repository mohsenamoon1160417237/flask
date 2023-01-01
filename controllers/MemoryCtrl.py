from models.MemoryMdl import MemoryMdl


class MemoryCtrl:

    def get_ram_info(self,num):
        mem_mdl = MemoryMdl()
        memory_datas = mem_mdl.get_data(num)
        return memory_datas
