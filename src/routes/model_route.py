from flask import Blueprint, jsonify, request, abort
import keras
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import numpy as np
from models.sentiment_response import SentimentResponse
from dataclasses import asdict, dataclass



main = Blueprint('movie_blueprint', __name__)

@main.errorhandler(400)
def handle_bad_request(error):
    response = jsonify({'error': error.description})
    response.status_code = 400
    return response

@main.route('/', methods=['POST'])
def predict():
        
    #cargar modelo
    loaded_model = keras.models.load_model("src/static/exported_model.h5")
    print("re", request.json)
    text = request.json['text']
    print("text-req", text)
    if len(text) == 0:
        abort(400, 'No se proporcionó el texto en la solicitud.')
    
    resultado = "neutral"
    twt = [text]
    max_fatures = 2000
    tokenizer = Tokenizer(num_words=max_fatures, split=' ')
    #vectorizing the tweet by the pre-fitted tokenizer instance
    twt = tokenizer.texts_to_sequences(twt)
    #padding the tweet to have exactly the same shape as `embedding_2` input
    twt = pad_sequences(twt, maxlen=166, dtype='int32', value=0)
    print("OL", twt)
    
    sentiment = loaded_model.predict(twt,batch_size=1,verbose = 2)[0]
    print("sentiment", sentiment)
    print(np.argmax(sentiment))
    if(np.argmax(sentiment) == 0):
        print("NEGATIVE")
        resultado = "NEGATIVE"
    elif (np.argmax(sentiment) == 1):
        print("positive")
        resultado = "POSITIVE"
    else:
        print("NEUTRAL")
        
    sentiment_float = np.array(sentiment, dtype=np.float32)
    
    print("sentiment_float", sentiment_float[0].item())
        
    sentimentResponse = SentimentResponse(
        sentiment=resultado,
        negativePercentage=sentiment_float[0].item(),
        positivePercentage=sentiment_float[1].item(),
        neutralPercentage=sentiment_float[2].item()
    )
    
    print("sr", sentimentResponse)
    
    response_data = asdict(sentimentResponse)
    print("rd", response_data)
     
    
    return jsonify(sentimentResponse.__dict__)