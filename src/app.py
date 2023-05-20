from flask import Flask
from flask_cors import CORS
# Routes
from routes import model_route 

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def page_not_found(error):
    return "<h1>Not found</h1>", 404

if __name__ == '__main__':
    
    # routes
    app.register_blueprint(model_route.main, url_prefix='/api/model-nlp')
    
    
    app.register_error_handler(404, page_not_found )
    app.run(host="0.0.0.0", debug=True)