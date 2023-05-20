from flask import Blueprint, jsonify
import keras
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import numpy as np



main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def predict():
    
    #cargar modelo
    loaded_model = keras.models.load_model("../utils/exported_model.h5")
    
    resultado = "neutral"
    twt = [""" Come meet one of the beautiful gods of gambling. """]
    max_fatures = 2000
    tokenizer = Tokenizer(num_words=max_fatures, split=' ')
    #vectorizing the tweet by the pre-fitted tokenizer instance
    twt = tokenizer.texts_to_sequences(twt)
    #padding the tweet to have exactly the same shape as `embedding_2` input
    twt = pad_sequences(twt, maxlen=166, dtype='int32', value=0)
    print(twt)
    sentiment = loaded_model.predict(twt,batch_size=1,verbose = 2)[0]
    print("sentiment", sentiment)
    print(np.argmax(sentiment))
    if(np.argmax(sentiment) == 0):
        print("negative")
        resultado = "negative"
    elif (np.argmax(sentiment) == 1):
        print("positive")
        resultado = "positive"
    else:
        print("neutral")
    
    return jsonify({'message':resultado})