from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from types import SimpleNamespace
import json
import requests

bp = Blueprint('video_game_mod2', __name__)


@bp.route('/api_test')
def test():
    api_response = requests.get('https://api.dccresource.com/api/games/')
    # games = api_response.json()
    games = json.loads(api_response.content, object_hook=lambda d: SimpleNamespace(**d))
    return render_template('video_games_views/api_test.html', games=games)


@bp.route('/best_console')
def best_console():
    # Query for everything last 7, based on number of game copies sold globally

    api_response = requests.get('https://api.dccresource.com/api/games/')
    # games = api_response.json()
    games = json.loads(api_response.content, object_hook=lambda d: SimpleNamespace(**d))

    ps4sales = 0
    for game in games:
        if game.platform == "PS4" and game.year >= 2007:
            ps4sales += game.globalSales
    return render_template('video_games_views/best_console.html', ps4sales=ps4sales)


@bp.route('/search_result')
def search_result():
    pass


@bp.route('/custom_question')
def custom_question():
    pass
