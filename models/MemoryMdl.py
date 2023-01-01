from sqlalchemy import desc

from managements.DbsMan import DbsMan

_db_memory = DbsMan.get_db_memory()


class MemoryMdl(_db_memory.Model, DbsMan):
    __tablename__ = "memory_data"
    my_db = _db_memory

    serialize_only = ('id', 'total', 'free', 'used')

    total = my_db.Column(my_db.Float)
    free = my_db.Column(my_db.Float)
    used = my_db.Column(my_db.Float)
    id = my_db.Column('memory_data_id', my_db.Integer, primary_key=True)

    def __init__(self, total=None, free=None, used=None):
        self.total = total
        self.free = free
        self.used = used

    def get_data(self, num=0):
        if num:
            memory_datas = self.query.order_by(desc(MemoryMdl.id)).limit(num).all()
        else:
            memory_datas = self.query.all()

        records = []
        for e_mem in memory_datas:
            fields = {}
            for field in list(self.serialize_only):
                fields[field] = e_mem.__getattribute__(field)
            records.append(fields)

        return records


    def save_to_db(self):
        self.my_db.session.add(self)
        self.my_db.session.commit()
