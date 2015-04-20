__author__ = 'gregory'

import random
from sys import exit



people = ['Professor Plum', 'Miss Scarlet', 'Miss Peacock', 'Mr. Green', 'Colonel Mustard', 'Mrs. White']
weapons = ['Revolver', 'Candlestick', 'Rope', 'Lead Pipe', 'Knife', 'Wrench']
rooms = ["Hallway", "Dining Room", "Study", "Conservatory", "Kitchen", "Ballroom", "Library", "Billiard Room", "Lounge"]
room_actions = {'1':'Guess','2':'Accuse','3':'Change Rooms'}
answer_person = random.choice(people)
answer_weapon = random.choice(weapons)
answer_room = random.choice(rooms)



def guess_person():
    print("Choose someone from the list: %r" % (people))
    person_choice = raw_input('Guess who did it: ')

    while person_choice not in people:
        person_choice = raw_input('Choose someone from the list: ')

    return person_choice

def guess_weapon():
    print ("Choose a weapon from the list: %r" % (weapons))
    weapon_choice = raw_input('Guess a weapon: ')
    while weapon_choice not in weapons:
        weapon_choice = raw_input('Choose a weapon from the list: ')

    return weapon_choice

def lose():
    print "You have made a false accusation! You lose!"
    exit()

def win(x, y, z):
    print "You did it! It was " + x + " in the " + y.lower() + " with the " + z.lower() + "."
    exit()

def hint(x, y, z):
    hint_list = []
    if x != answer_person:
        hint_list.append(x)
    if y != answer_weapon:
        hint_list.append(y)
    if z != answer_room:
        hint_list.append(z)
    if len(hint_list) > 0:
        random_hint = random.choice(hint_list)
        if random_hint in people:
            print "Clue hint: It is not " + str(random_hint) + "."
        elif random_hint in weapons:
            print "Clue hint: It is not the " + str(random_hint) + "."
        else:
            print "Clue hint: It is not in the " + str(random_hint) + "."
    else:
        pass

def room_action():
    action_choice = raw_input("What would you like to do? Type 1 to guess, 2 to accuse, and 3 to change rooms: ")
    while action_choice != '1' and action_choice != '2' and action_choice != '3':
        action_choice = raw_input("What would you like to do? Type 1 to guess, 2 to accuse, and 3 to change rooms: ")
    return action_choice

def accuse_person():
    print("Here are the suspects: %r" % (people))
    person_choice = raw_input('Accuse the perpetrator of this heinous crime: ')

    while person_choice not in people:
        person_choice = raw_input('Choose someone from the list: ')

    return person_choice

def accuse_weapon():
    print("Here are the available weapons: %r" % (weapons))
    weapon_choice = raw_input('Pick the weapon: ')

    while weapon_choice not in weapons:
        weapon_choice = raw_input('Choose a weapon from the list: ')

    return weapon_choice

def accuse_room():
    print("Here are the potential rooms: %r" % (rooms))
    room_choice = raw_input('Where was the crime committed: ')

    while room_choice not in rooms:
        room_choice = raw_input('Choose a room from the list: ')

    return room_choice

def accuse():
    person = accuse_person()
    weapon = accuse_weapon()
    room = accuse_room()
    if person != answer_person or weapon != answer_weapon or room != answer_room:
        lose()
    else:
        win(person, room, weapon)


