from flask import Blueprint, request
import json

from controllers.game import *

game_view = Blueprint('game', __name__, url_prefix='/game')

@game_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_game()
    else:
        
        submitted_data = json.dumps(request.data.decode())
        submitted_data = json.loads(submitted_data)
        
        print(submitted_data)
        
        save_game.json.fdumps(game)
        # files = request.files.getlist("files"
        

        # results = (
        #     submitted_data['results']
        # )

        # return save_game(results, uploaded_files=files)
        
        
        return "The stuff is in progress"
    
@game_view.route('/<id>', methods=['GET', 'POST'])
def get_or_update_instance(id):
    if request.method == 'GET':
        return get_game_with_id(gameId)
    pass