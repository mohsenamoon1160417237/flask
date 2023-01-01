from managements.DbsMan import DbsMan

_dbMemory = DbsMan.getDbMemory()


class MemoryMdl(_dbMemory.Model,DbsMan):  # remind: wrong extend to db.Model
    __tablename__ = "memory_data"
    myDb = _dbMemory

    serialize_only = ('id', 'total', 'free', 'used')

    total = myDb.Column(myDb.Float)
    free = myDb.Column(myDb.Float)
    used = myDb.Column(myDb.Float)
    id = myDb.Column('memory_data_id', myDb.Integer, primary_key=True)

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
        self.myDb.session.add(self)  # todo self?
        self.myDb.session.commit()

