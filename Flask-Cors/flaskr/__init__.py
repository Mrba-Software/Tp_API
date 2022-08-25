# Import Dependencies
from flask import Flask, jsonify, request
from models import setup_db, Plant, db
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers pour controler les requetes dans l'appli:
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    
    @app.route('/plants')
    #pour un controle de requete specifique a une route, on ajoute:
    #@cross_origin()
    #puis on met la fonction qui gere la route:
    def get_plants():
        page = request.args.get('page',1,type=int)
        start = (page-1)*10
        end = start+10
        plants = Plant.query.all()
        #ON PASE L'OBJET PlAnt A LA FONCTION format() POUR LE RENDRE LISIBLE PAR L'utilisateur: 
        formatted_plants = [plants.format() for plant in plants]

        return jsonify({
            'Succes':'True',
            'plants':formatted_plants[start:end],
            'total_plants':len(formatted_plants)
        })

    return app