from config import app, db
from routes.cities import cities_bp
from update_data import update_data
app.register_blueprint(cities_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        update_data()
    app.run(debug=False)