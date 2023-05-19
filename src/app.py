from flask import Flask

# Routes
from routes import model_route 

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found</h1>", 404

if __name__ == '__main__':
    
    # routes
    app.register_blueprint(model_route.main, url_prefix='/api/model-nlp')
    
    
    app.register_error_handler(404, page_not_found )
    app.run(host="0.0.0.0")