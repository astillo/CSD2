# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, playerName, room):
        self.playerName = playerName
        self.room = room

    def __str__(self):
        return f'Player(Player Name: {self.playerName}, current room: {self.room})'

    def move(self, newRoom):
        self.room = newRoom
