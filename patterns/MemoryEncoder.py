import json

from sqlalchemy.ext.declarative import DeclarativeMeta


class MemoryEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if
                          not x.startswith('_') and x != 'metadata' and x in ["free", "total", "id", "used"]]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)
