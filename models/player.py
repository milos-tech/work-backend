import sqlite3


class Player():
    TABLE_NAME = "Player"
    PATH_TO_DB = "chess.db"

    def __init__(self, playerId=None, player_name=None) -> None:
        self.playerId = playerId
        self.player_name = player_name

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as conn:
            cursor = conn.cursor()

            if self.playerId:
                query = f"UPDATE {self.__class__.TABLE_NAME} SET player_name=? WHERE playerId=?"
                
                cursor.execute(
                    query,
                    (self.player_name, self.playerId)
                )
            else:
                # save into the database
                query = f"INSERT INTO {self.TABLE_NAME} (player_name) VALUES (?)"

                cursor.execute(
                    query, 
                    (self.player_name)
                )

                # get the newly created record's id
                playerId = cursor.execute(f"SELECT MAX(id) FROM {self.TABLE_NAME}").fetchone()[0]

                self.playerId = playerId

    def read(playerId=None):
        with sqlite3.connect(PATH_TO_DB) as conn:
            cursor = conn.cursor()

            if playerId:
                result = cursor.execute(f"SELECT playerId, player_name FROM {__class__.TABLE_NAME} WHERE playerId=?", (playerId, )).fetchone()

                player = __class__(playerId=result[0], player_name=result[1])

                return player
            else:
                results = cursor.execute(f"SELECT playerId, player_name FROM {__class__.TABLE_NAME}").fetchall()
                
                player = []
                
                for result in results:
                    exam = __class__(playerId=result[0], player_name=result[1])
                    player.append(player)

                return player

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as conn:
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE playerId=?", (self.playerId,))

        self.playerId = None
