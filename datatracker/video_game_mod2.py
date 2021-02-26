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
    api_response = requests.get('https://api.dccresource.com/api/games/')

    games = json.loads(api_response.content, object_hook=lambda d: SimpleNamespace(**d))

    recent_games = []

    for game in games:
        if game.year is not None and game.year >= 2013:
            recent_games.append(game)

    platform_totals = {
        'PS3': 0,
        'PS4': 0,
        'X360': 0,
        'XOne': 0,
        'PC': 0,
        'Wii': 0,
        'WiiU': 0,
        '3DS': 0,
        'PSV': 0,
        'PSP': 0
    }

    for game in recent_games:
        if game.platform == 'PS3':
            platform_totals['PS3'] += game.globalSales
        elif game.platform == 'PS4':
            platform_totals['PS4'] += game.globalSales
        elif game.platform == 'X360':
            platform_totals['X360'] += game.globalSales
        elif game.platform == 'XOne':
            platform_totals['XOne'] += game.globalSales
        elif game.platform == 'PC':
            platform_totals['PC'] += game.globalSales
        elif game.platform == 'Wii':
            platform_totals['Wii'] += game.globalSales
        elif game.platform == 'WiiU':
            platform_totals['WiiU'] += game.globalSales
        elif game.platform == '3DS':
            platform_totals['3DS'] += game.globalSales
        elif game.platform == 'PSV':
            platform_totals['PSV'] += game.globalSales
        elif game.platform == 'PSP':
            platform_totals['PSP'] += game.globalSales

    return render_template('video_games_views/best_console.html', platform_totals=platform_totals)


@bp.route('/search_result', methods=['GET'])
def search_result():
    if request.method == 'GET':
        return render_template('video_games_views/search_result.html')

    # user_input = request.form['title'].lower()

    # if request.method == 'POST':
    #     api_response = requests.get('https://api.dccresource.com/api/games/')
    #     games = json.loads(api_response.content, object_hook=lambda d: SimpleNamespace(**d))
    #
    #     for game in games:
    #         if game.name.lower() == user_input:
    #             searchmatch = game
    #
    #     return render_template('video_games_views/game_detail', searchmatch=searchmatch)


@bp.route('/game_detail', methods=['POST'])
def game_detail():
    if request.method == 'POST':
        user_input = request.form['title'].lower()
        api_response = requests.get('https://api.dccresource.com/api/games/')
        games = json.loads(api_response.content, object_hook=lambda d: SimpleNamespace(**d))

        for game in games:
            if game.name.lower() == user_input:
                searchmatch = game

        return render_template('video_games_views/game_detail', searchmatch=searchmatch)


@bp.route('/custom_question')
def custom_question():
    pass
