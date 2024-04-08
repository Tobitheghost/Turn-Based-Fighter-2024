from flask import Flask

def create_app():
    app = Flask(__name__)

    from .index import game_bp
    app.register_blueprint(game_bp)
    return app

from fighter.versions.website import index

if __name__ == '__main__':
    create_app()