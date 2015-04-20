__author__ = 'gregory'

from Functions_and_Variables import Functions
from Rooms import Rooms
from sys import exit

#print(answer_person + ' ' + answer_weapon + ' ' + answer_room)
print '''Welcome to Clue!
John Body has been cruelly murdered, and it is up to you to solve the crime.
Here are the rules:
Navigate through the rooms and guess in each room.
You can only guess once in a room.
You do not have to guess if you are in a room. You will have the option to
go to the next room.
If you guess in a room, your guess will be for the room you are in.
You will get hints along the way.
You will also have the option to accuse at any point in the game,
but be careful, a false accusation will make you lose!'''

if raw_input('Would you like to play? (y/n)' ) == "y":
    person = ''
    weapon = ''
    active_room = Rooms.start.current_room()
    room = active_room.room_name

    while person != Functions.answer_person or weapon != Functions.answer_weapon or room != Functions.answer_room:
        active_room.enter_room()
        room = active_room.room_name
        action = Functions.room_action()
        if action == '1':
            person = Functions.guess_person()
            weapon = Functions.guess_weapon()
            Functions.hint(person, weapon, active_room.room_name)
            if person == Functions.answer_person \
                    and weapon == Functions.answer_weapon and active_room.room_name == Functions.answer_room:
                Functions.win(person, active_room.room_name, weapon)
            else:
                pass
            new_active = active_room.change_room()
            active_room = new_active
        elif action == '2':
            Functions.accuse()
        else:
            new_active = active_room.change_room()
            active_room = new_active

    Functions.win(person, active_room.room_name, weapon)
else:
    print "Bye!"
    exit()