__author__ = 'gregory'


class Room(object):

    '''All rooms have greeting, instructions, direction_choice, direction instructions, room instructions, and room name.
    Dictionary that lists direction and corresponding room.'''
    current_room = ''

    def __init__(self,room_name):
        self.greeting = "You are now in the %s." % room_name
        self.room_name = room_name
        self.connecting_rooms = {}


    def connect_rooms(self,connecting_rooms):
        self.connecting_rooms.update(connecting_rooms)

    def enter_room(self):
        print(self.greeting)


    def change_room(self):
        print("There are " + str(len(self.connecting_rooms)) + " rooms connected to the " + self.room_name + ".")
        for key, value in sorted(self.connecting_rooms.items()):
            if key == 'trapdoor':
                print("A secret " + str(key) + " leads to the " + value.room_name + ".")
            else:
                print("Door " + str(key) + " leads to the " + value.room_name + ".")

        dir_choice = raw_input("Choose your door: ")
        while dir_choice not in self.connecting_rooms:
            dir_choice = raw_input("Choose a door from the list: ")
        for key, value in self.connecting_rooms.items():
            if dir_choice == key:
                return value

    def current_room(self):
        return self


Hallway = Room("Hallway")
Ballroom = Room("Ballroom")
Library = Room("Library")
Lounge = Room("Lounge")
Conservatory = Room("Conservatory")
Kitchen = Room("Kitchen")
Dining_Room = Room("Dining Room")
Billiard_Room = Room("Billiard Room")
Study = Room("Study")



Hallway.connect_rooms({'1':Ballroom,'trapdoor':Study})
Ballroom.connect_rooms({'1':Library,'2':Dining_Room,'3':Lounge,'4':Hallway})
Library.connect_rooms({'1':Lounge, '2':Study,'3':Ballroom})
Study.connect_rooms({'1':Library, '2':Billiard_Room, 'trapdoor':Hallway})
Billiard_Room.connect_rooms({'1':Conservatory, '2':Lounge, '3':Study})
Lounge.connect_rooms({'1':Billiard_Room,'2':Library, '3': Conservatory, '4':Ballroom})
Conservatory.connect_rooms({'1':Lounge,'2':Billiard_Room,'trapdoor':Kitchen})
Dining_Room.connect_rooms({"1":Kitchen, "2":Ballroom})
Kitchen.connect_rooms({"1":Dining_Room,"trapdoor":Conservatory})

start = Hallway

