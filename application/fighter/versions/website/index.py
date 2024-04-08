from flask import render_template, Blueprint

game_bp = Blueprint('game',__name__,url_prefix="/")

@game_bp.route('/')
def index():
    return render_template("game.html")
