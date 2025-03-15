from config import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True, unique=True)
    cost_of_living = db.Column(db.Float, nullable=True)
    population = db.Column(db.Integer, nullable=True)

    def to_json(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }