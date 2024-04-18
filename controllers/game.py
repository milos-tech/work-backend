import os
import sys
current_dir=os.getcwd()
sys.path.append(current_dir)

from models.game import Game

from constants import UPLOAD_FOLDER

def get_game():
    games = Game.read()   
    game_list = [key.toJSON() for key in games]
    
    return game_list

def get_game_with_id(gameId):
    return Game.read(gameId)

def save_game(gameId=None, results=None):
    
    if gameId != None:
        
        game = get_game_with_id(self, gameId)
        return game.toJSON()
        
        
    else:
        game = Game(
            results=results
        )

    game.save()

    for file in uploaded_files:
        file_name = secure_filename(file.filename)

        save_file(game=game.gameId, path=file_name)

        file.save(
            os.path.join(UPLOAD_FOLDER, file_name)
        )

    return game
    
def delete_game(gameId):
    game = get_game_with_id(gameId)
    game.delete()

