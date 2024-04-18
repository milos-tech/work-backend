import os
import sys
current_dir=os.getcwd()
sys.path.append(current_dir)

from models.player import Player

from constants import UPLOAD_FOLDER

def get_all_player():
    return Player.read()

def get_player_with_id(gameId):
    return Player.read(gameId)

def save_player(playerId=None, player_name=None):
    if playerId != None:
        player = get_game_with_id(playerId)
        player.player_name = (
            player_name
        )
    else:
        player = Player(
            player_name=player_name
        )

    player.save()

    for file in uploaded_files:
        file_name = secure_filename(file.filename)

        save_file(player=player.playerId, path=file_name)

        file.save(
            os.path.join(UPLOAD_FOLDER, file_name)
        )

    return game
    
def delete_player(playerId):
    player = get_player_with_id(playerId)
    player.delete()