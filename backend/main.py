from flask import request, jsonify
from config import app, db
from models import City
from update_data import update_data

@app.route("/cities", methods=["GET"])
def get_cities():
    cities = City.query.all()
    json_cities = list(map(lambda x: x.to_json(), cities))
    return jsonify({"cities": json_cities})

@app.route("/create_cities", methods=["POST"])
def create_city():
    name = request.json.get("name")
    cost_of_living = request.json.get("costOfLiving")
    population = request.json.get("population")

    if not name or not cost_of_living or not population:
        return jsonify({"message": "You did not include a name, cost of living or population"}), 400

    new_city = City(name=name, cost_of_living=cost_of_living, population=population)
    try:
        db.session.add(new_city)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "City created!"}), 201

@app.route("/update_city/<int:city_id>", methods=["PATCH"])
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

@app.route("/delete_city/<int:city_id>", methods=["DELETE"])
def delete_city(city_id):
    city = City.query.get(city_id)

    if not city:
        return jsonify({"message": "City not found"}), 404
    
    db.session.delete(city)
    db.session.commit()

    return jsonify({"message": "City deleted"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        update_data()
        
    app.run(debug=True)