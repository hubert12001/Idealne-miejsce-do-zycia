from flask import Blueprint, request, jsonify
from config import db
from models.city import City

cities_bp = Blueprint("cities", __name__)

@cities_bp.route("/cities", methods=["GET"])
def get_cities():
    cities = City.query.all()
    json_cities = [city.to_json() for city in cities]
    return jsonify({"cities": json_cities})


# POST, PATCH, DELETE (Jak narazie nie uzywane)
"""
@cities_bp.route("/create_city", methods=["POST"])
def create_city():
    data = request.json
    name = data.get("name")
    cost_of_living = data.get("costOfLiving")
    population = data.get("population")

    if not name or cost_of_living is None or population is None:
        return jsonify({"message": "You must provide name, costOfLiving, and population"}), 400

    new_city = City(name=name, cost_of_living=cost_of_living, population=population)
    try:
        db.session.add(new_city)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "City created!"}), 201

@cities_bp.route("/update_city/<int:city_id>", methods=["PATCH"])
def update_city(city_id):
    city = City.query.get(city_id)

    if not city:
        return jsonify({"message": "City not found"}), 404
    
    data = request.json
    city.name = data.get("name", city.name)
    city.cost_of_living = data.get("costOfLiving", city.cost_of_living)
    city.population = data.get("population", city.population)

    db.session.commit()

    return jsonify({"message": "City updated"}), 200

@cities_bp.route("/delete_city/<int:city_id>", methods=["DELETE"])
def delete_city(city_id):
    city = City.query.get(city_id)

    if not city:
        return jsonify({"message": "City not found"}), 404
    
    db.session.delete(city)
    db.session.commit()

    return jsonify({"message": "City deleted"}), 200
"""