import sqlite3

class Gp:
    def __init__(self, gpId = None, playerId = None, gameId = None):
        self.gpId = gpId
        self.playerId = playerId
        self.gameId = gameId
        
    def save(self):
        #insert or updating the database
            
            if self.gpId:
                #update
                query = f"UPDATE {self.__class__.TABLE_NAME} SET playerId=?, gameId=?"
                
                with sqlite3.connect("chess.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute(query, (self.playerId, self.gameId))
            else:
                #insert or save into the database
                query = f"INSERT INTO {self.__class__.TABLE_NAME}(playerId, gameId) VALUES(?, ?)"
                with sqlite3.connect("chess.db") as conn:
                    Cursor = conn.cursor()
                    cursor.execute(query, (self.playerId, self.gameId))
                
                new_instance_gameId = cursor.execute(f"SELECT MAX(playerId, gameId) FROM {self.__class__.TABLE_NAME}").fetchone()[0]
                
                self.gpId = new_instance_gpId
                
    def read(self, gpId=None, playerId=None, gameId=None):
            with sqlite3.connect("chess.db") as conn:
                cursor = conn.cursor()
            
            if gameId:
                query = f"SELECT (gpId, playerId, gameId) FROM {self.__class__.TABLE_NAME} WHERE gameId=?"
                
                result = cursor.execute(query, (id, )).fetchone()
                
                gp = Gp(playerId=result[1], gameId=result[2])
                gp.gpId = result[0]
                
                return game
            else:
                query = f"SELECT (gpId, playerId, gameId) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                gp = []
                
                for result in results:
                    gp = Gp(playerId=result[1], gameId=result[2])
                    gp.gpId = result[0]
                    
                    game.append(game)
                    
                return player_game
    def delete(self):
        if self.gpId:
            with sqlite3.connect("chess.db") as conn:
                cursor = conn.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE gpId=?", (self.gpId, ))