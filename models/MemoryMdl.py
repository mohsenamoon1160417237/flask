from managements.DbsMan import DbsMan

DbsMan.readyDbMemory()


class MemoryMdl(DbsMan.dbMemory.Model,DbsMan):  # remind: wrong extend to db.Model
    __tablename__ = "memory_data"
    __myDb__ = DbsMan.dbMemory

    serialize_only = ('id', 'total', 'free', 'used',)

    total = DbsMan.dbMemory.Column(DbsMan.dbMemory.Float)
    free = DbsMan.dbMemory.Column(DbsMan.dbMemory.Float)
    used = DbsMan.dbMemory.Column(DbsMan.dbMemory.Float)
    id = DbsMan.dbMemory.Column('memory_data_id', DbsMan.dbMemory.Integer, primary_key=True)

    def __init__(self , total=None, free=None, used=None):
        self.total = total
        self.free = free
        self.used = used

    def get_data(self,num=0):
        memory_datas = self.__dbMdl.query.all()  # todo chk query by num
        if num:
            memory_datas = memory_datas[::-1][:num]

        return memory_datas

    def saveToDb(self):
        self.__myDb__.session.add(self)  # todo self?
        self.__myDb__.session.commit()

