from room import Room
from player import Player
import textwrap

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

# print("Start the Adventure!!!")

   

# Make a new player object that is currently in the 'outside' room.
player1 = Player("John", room["outside"])
# player2 = Player("player1", room["outside"])
# print(player1.name)
# print(player1.current_room.name)
# print(player1.current_room.n_to)

# print(player1.name)
# print(player1.current_room)
# print(player1.current_room)
# print(player1.current_room)

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
while True:
    print(player1.current_room.name)
    print(textwrap.fill(player1.current_room.description))

    direction = input("Where do you what to go?:")
    if room['outside'] and direction is "north".lower() or "n".lower():
        print(room['foyer'].name)
        print(room['foyer'].description)
        continue
    elif room['foyer'] and direction is "south".lower() or "s".lower():
        print(room['outside'].name)
        print(room['outside'].description)
        
    elif room['foyer'] and direction is "nouth".lower() or "n".lower():
        print(room['overlook'].name)
        print(room['overlook'].description)
        
    elif room['foyer'] and direction is "east".lower() or "e".lower():
        print(room['narrow'].name)
        print(room['narrow'].description)
        
    elif room['overlook'] and direction is "south".lower() or "s".lower():
        print(room['foyer'].name)
        print(room['foyer'].description)
        
    elif room['narrow'] and direction is "west".lower() or "w".lower():
        print(room['foyer'].name)
        print(room['foyer'].description)
        
    elif room['narrow'] and direction is "north".lower() or "n".lower():
        print(room['treasure'].name)
        print(room['treasure'].description)
        
    elif room['treasure'] and direction is "south".lower() or "s".lower():
        print(room['narrow'].name)
        print(room['narrow'].description)
        break