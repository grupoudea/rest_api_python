from flask import Blueprint, jsonify

main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def predict():
    return jsonify({'message':"HOLA"})