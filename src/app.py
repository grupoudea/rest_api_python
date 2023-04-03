from flask import Flask
from config import config

# Routes
from routes import movie_route 

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    # routes
    app.register_blueprint(movie_route.main, url_prefix='/api/movies')
    
    app.register_error_handler(404, page_not_found )
    app.run()