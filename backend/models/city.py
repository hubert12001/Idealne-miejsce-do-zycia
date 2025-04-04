from config import db
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.sqlite import JSON

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True, unique=True)
    parameters = db.Column(MutableDict.as_mutable(JSON), nullable=False, default={})

    def to_json(self):
        return {
            "miasto": self.name,
            "parametry": self.parameters
        }