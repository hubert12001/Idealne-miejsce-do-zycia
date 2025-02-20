from config import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    cost_of_living = db.Column(db.Float, nullable=True)
    population = db.Column(db.Integer, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "costOfLiving": self.cost_of_living,
            "population": self.population
        }