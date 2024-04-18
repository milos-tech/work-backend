import os
import sys
current_dir=os.getcwd()
sys.path.append(current_dir)

from models.playergame import Gp

from constants import UPLOAD_FOLDER

def get_all_playergame():
    return Gp.read()

def get_playergame_with_id(gpId):
    return Gp.read(gpId)

def save_player_game(gpId=None, playerId=None, gameId=None):
    if gpId != None:
        playergame = get_playergame_with_id(gpId)
        playergame.playerId, playergame.gameId = (
            playerId, gameId
        )
    else:
        playergame = Gp(
            playerId=playerId,gameId=gameId
        )

    playergame.save()

    for file in uploaded_files:
        file_name = secure_filename(file.filename)

        save_file(playergame=playergame.gpId, path=file_name)

        file.save(
            os.path.join(UPLOAD_FOLDER, file_name)
        )

    return game
    
def delete_playergame(gpId):
    playergame = get_playergame_with_id(gpId)
    playergame.delete()