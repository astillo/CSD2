from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user = Player(input('What is your name?'), room['outside'])

hasQuit = False

welcome_text = f"""Welcome to BattleInfinity {user.playerName}!!\n Using NSEW keys please indicate the direction youd like to move \n"""

print(welcome_text)

is_loser = False

while not is_loser:
    current_room = user.room
    print(f'{current_room.room_name}: {current_room.description} \n')
    user_direction = input('Please select a way to move').upper()

    room_directions = {
        'N': current_room.n_to,
        'S': current_room.s_to,
        'E': current_room.e_to,
        'W': current_room.w_to
    }

    if user_direction == 'Q':
        is_loser = True
        print(f'It has been a pleasure {user.playerName}')

    elif user_direction == 'N' or user_direction == 'S' or user_direction == 'E' or user_direction == 'W':
        user.move(room_directions[user_direction])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
