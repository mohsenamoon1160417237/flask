


class MemoryData:  # remind: wrong extend to db.Model
    __tablename__ = "memory_data"

    serialize_only = ('id', 'total', 'free', 'used',)

    def __init__(self ,db , total, free, used):
        self.total = total
        self.free = free
        self.used = used
        self.id = db.Column('memory_data_id', db.Integer, primary_key=True)
        self.total = db.Column(db.Float)
        self.free = db.Column(db.Float)
        self.used = db.Column(db.Float)
        self.dbMdl = db.Model
        self.db = db

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.dbMdl.__table__.columns}

    def saveToDb(self):
        self.db.session.add(self.dbMdl)  # todo self | self.dbMdl ?
        self.db.session.commit()

