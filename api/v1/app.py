#!/usr/bin/python3
from flask import Flask, make_response, jsonify
from models import storage
from os import environ
from api.v1.views import app_views
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):

    return make_response(jsonify({"error": "Not found"}), 404)

@app.teardown_appcontext
def teardown(error):
    """ Call storage.close() """
    return storage.close()


if __name__=="__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = "0.0.0.0"
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
#Cors
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
