from flask import Blueprint, jsonify, request, abort
import keras
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import numpy as np
from dataclasses import asdict

from models.sentiment_response import SentimentResponse

import pickle

main = Blueprint('movie_blueprint', __name__)


@main.errorhandler(400)
def handle_bad_request(error):
    response = jsonify({'error': error.description})
    response.status_code = 400
    return response


@main.route('/', methods=['POST'])
def predict():
    # Cargar el modelo
    loaded_model = keras.models.load_model("src/static/exported_model.h5")

    with open('src/static/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Obtener el texto de la petición
    text = request.json.get('text')

    # Validar si se proporcionó texto en la peticións
    if not text:
        abort(400, 'No se proporcionó el texto en la petición.')

    # Procesar el texto
    resultado = "NEUTRAL"
    twt = [text]

    # Limpiar los datos
    twt = np.char.lower(twt)
    twt = np.char.replace(twt, '[^a-zA-Z0-9\s]', '')
    twt = np.char.replace(twt, '@', '')
    print('twt = ',twt)

    # Tokenizer
    tokens = tokenizer.texts_to_sequences(twt)
    print(tokens)   
    tokens_padded = pad_sequences(tokens, maxlen=166)
    print(tokens_padded)

    # Predecir el sentimiento
    sentiment = loaded_model.predict(tokens_padded, batch_size=1, verbose=2)[0]
    print(sentiment)
    if np.argmax(sentiment) == 0:
        resultado = "NEGATIVE"
    elif np.argmax(sentiment) == 1:
        resultado = "POSITIVE"

    sentiment_float = np.array(sentiment, dtype=np.float32)

    # Crear la respuesta de sentimiento
    sentiment_response = SentimentResponse(
        sentiment=resultado,
        negativePercentage=sentiment_float[0].item(),
        positivePercentage=sentiment_float[1].item(),
        neutralPercentage=sentiment_float[2].item()
    )

    # Convertir la respuesta a un diccionario
    response_data = asdict(sentiment_response)

    return jsonify(response_data)
