import json

from utility.db.MemoryData import MemoryData
from utils import AlchemyEncoder


class RamCtrl:

    def __init__(self,db):
        self.db = db
        self.dbMdl = db.Model

    def getRamInfo(self,num):
        if num is not None:
            num = int(num)
            memory_datas = self.dbMdl.query.all()[::-1][:num]
        else:
            memory_datas = self.dbMdl.query.all()
        return json.dumps(memory_datas, cls=AlchemyEncoder)
        # return memory_datas.to_dict()
        # return memory_datas