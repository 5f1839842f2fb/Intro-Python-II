from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
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

player = Player('John')
player.location = room['outside']

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

inp = ''
while inp != 'q':
    print("\n"+player.location.fullname+ " - " +player.location.description+"\n ")
    print("Enter direction (n s e w) or q to quit")

    try:
        inp = input()
        if inp == 'n':
            player.location = room[player.location.name].n_to
        elif inp == 's':
            player.location = room[player.location.name].s_to
        elif inp == 'e':
            player.location = room[player.location.name].e_to
        elif inp == 'w':
            player.location = room[player.location.name].w_to
    except:
        print("Invalid direction")
    
