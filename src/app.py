"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Planets, Characters, Favorites_Characters, Favorites_Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    all_users = Users.query.all()
    all_users_list = list(map(lambda users: users.serialize(),all_users))

    return jsonify(all_users_list), 200

@app.route('/Planets', methods=['GET'])
def get_planets():
    all_planets = Planets.query.all()
    results = list(map(lambda planet: planet.serialize(),all_planets))

    return jsonify(results), 200

@app.route('/Characters', methods=['GET'])
def get_characters():
    all_characters = Characters.query.all()
    results = list(map(lambda characters: characters.serialize(),all_characters))

    return jsonify(results), 200

@app.route('/Favorites_Characters', methods=['GET'])
def get_favcharacter():
    all_favcharacters = Favorites_Characters.query.all()
    results = list(map(lambda Favorites_Characters: Favorites_Characters.serialize(),all_favcharacters))

    return jsonify(results), 200

@app.route('/Favorites_Planets', methods=['GET'])
def get_favplanets():
    all_favplanets = Favorites_Planets.query.all()
    results = list(map(lambda Favorites_Planets: Favorites_Planets.serialize(),all_favplanets))

    return jsonify(results), 200

@app.route('/Favorites_Planets', methods=['POST '])
def create_favplanets():
    data = request.get_json()

    all_favplanets = Favorites_Planets.query.all()
    results = list(map(lambda Favorites_Planets: Favorites_Planets.serialize(),all_favplanets))

    return jsonify(results), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
