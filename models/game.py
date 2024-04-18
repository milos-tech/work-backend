import os
import sqlite3
from .Db_config import PATH_TO_DB

class Game():
    TABLE_NAME = "game"

    def __init__(self, gameId=None, results=None) -> None:
        self.gameId = gameId
        self.results = results
        
    def create_table(self):
        pass

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as conn:
            cursor = conn.cursor()

            if self.gameId:
                query = f"UPDATE {self.__class__.TABLE_NAME} SET results=? WHERE gameId=?"
                
                cursor.execute(
                    query,
                    (self.results, self.gameId)
                )
            else:
                # save into the database
                query = f"INSERT INTO {self.TABLE_NAME} (results) VALUES ('Chess Player')"

                cursor.execute(query)
                
                conn.commit()
                # get the newly created record's id
                gameId = cursor.execute(f"SELECT MAX(gameId) FROM {self.TABLE_NAME}").fetchone()[0]

                self.gameId = gameId
                
                return True, "Inserted successfully"

    def read(gameId=None):
        with sqlite3.connect(PATH_TO_DB) as conn:
            cursor = conn.cursor()

            if gameId:
                query = f"SELECT gameId, results FROM {__class__.TABLE_NAME} WHERE gameId = {gameId}"
                result = cursor.execute(query).fetchone()
                
                conn.commit()

                game = __class__(gameId=result[0], results=result[1])

                return game
            else:
                resultat = cursor.execute(f"SELECT gameId, results FROM {__class__.TABLE_NAME}").fetchall()
                
                game = []
                
                for result in resultat:
                    game_item = __class__(gameId=result[0], results=result[1])
                    game.append(game_item)

                return game

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as conn:
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE gameId=?", (self.gameId,))

        self.gameId = None
        

    def toJSON(self):
        return {
            "Id" : self.gameId,
            "Result": self.results
        }
