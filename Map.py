#Program Name: Map class for Porter Maps
#Program Authors: Anuva Nath, Sulagna Saha, Safia Safia
#Date: January 15, 2025
#Program Description: This class creates a map using the classes
#Floor1ClassRoom and Floor2ClassRoom, it makes objects for the stairs and
#classrooms found on both floors and has methods to help find the path from
#one room to another


from Floor1ClassRoom import Floor1ClassRoom
from Floor2ClassRoom import Floor2ClassRoom

class Map ():
    def __init__ (self):
        #initializes all components of the map
        self.floor_1rooms = {}
        self.floor_1stairs = {}
        self.floor_2rooms = {}
        self.floor_2stairs = {}
        
        #adds all classrooms on both floors
        self.add_floor1_classrooms()
        self.add_floor2_classrooms()
        
        self.visited = set()#set of visited cells on the grid
        self.map = []#floor map
        self.floor_dict = {}#dictionary of floor objects
        self.floor = 1#floor number

    #adds classrooms in floor1
    def add_floor1_classrooms (self):
        #rooms
        self.add_floor1_room ("116", 14, 2)
        self.add_floor1_room ("115", 13, 2)
        self.add_floor1_room ("114", 9, 2)
        self.add_floor1_room ("113", 10, 4)
        self.add_floor1_room ("112", 10, 5)
        self.add_floor1_room ("111", 10, 8)
        self.add_floor1_room ("110", 10, 9)
        self.add_floor1_room ("109", 10, 10)
        self.add_floor1_room ("108", 10, 12)
        self.add_floor1_room ("107", 11, 15)
        self.add_floor1_room ("106", 14, 15)
        self.add_floor1_room ("105", 15, 11)
        self.add_floor1_room ("104", 16, 15)
        self.add_floor1_room ("103", 20, 15)
        self.add_floor1_room ("102", 23, 13)
        self.add_floor1_room ("101", 23, 10)
        self.add_floor1_room ("100", 23, 7)
        self.add_floor1_room ("IT1", 9, 15)
        self.add_floor1_room ("IT2", 5, 19)
        self.add_floor1_room ("IT3", 3, 19)
        self.add_floor1_room ("IT4", 3, 22)
        self.add_floor1_room ("IT5", 3, 25)
        self.add_floor1_room ("IT6", 3, 27)
        self.add_floor1_room ("IT7", 3, 26)
        self.add_floor1_room ("IT8", 3, 28)
        self.add_floor1_room ("Small Gym", 18, 24)
        self.add_floor1_room ("Big Gym", 17, 15)
        self.add_floor1_room ("Music Room", 20, 21)
        self.add_floor1_room ("Swimming Pool", 13, 22)

        #stairs - considers stairs to be a room too
        #gets the stairs from the floor1  class
        self.floor_1stairs = self.floor_1rooms ["100"].get_floor_stairs ()
        for key in self.floor_1stairs:
            door_coordinates = self.floor_1stairs [key]
            new_key = "floor1" + key
            self.add_floor1_room (new_key, door_coordinates[0], door_coordinates[1])

    #adds classrooms in floor2
    def add_floor2_classrooms (self):
        #rooms
        self.add_floor2_room ("201", 25, 11)
        self.add_floor2_room ("202", 25, 11)
        self.add_floor2_room ("203", 25, 14)
        self.add_floor2_room ("204", 25, 13)
        self.add_floor2_room ("205", 25, 17)
        self.add_floor2_room ("207", 21, 19)
        self.add_floor2_room ("208", 25, 17)
        self.add_floor2_room ("209", 16, 19)
        self.add_floor2_room ("210", 14, 24)
        self.add_floor2_room ("211", 15, 19)
        self.add_floor2_room ("212", 14, 25)
        self.add_floor2_room ("214", 11, 19)
        self.add_floor2_room ("215", 6, 19)
        self.add_floor2_room ("216", 9, 19)
        self.add_floor2_room ("217", 5, 19)
        self.add_floor2_room ("218", 7, 19)
        self.add_floor2_room ("220", 4, 19)
        self.add_floor2_room ("224", 2, 19)
        self.add_floor2_room ("225", 10, 16)
        self.add_floor2_room ("226", 10, 13)
        self.add_floor2_room ("227", 10, 13)
        self.add_floor2_room ("228", 10, 11)
        self.add_floor2_room ("229", 10, 11)
        self.add_floor2_room ("230", 10, 7)
        self.add_floor2_room ("231", 10, 9)
        self.add_floor2_room ("232", 10, 5)
        self.add_floor2_room ("233", 10, 7)
        self.add_floor2_room ("234", 10, 4)
        self.add_floor2_room ("235", 11, 4)
        self.add_floor2_room ("236", 15, 4)

        #stairs - considers stairs to be a room too
        #gets the stairs from the floor1  class
        self.floor_2stairs = self.floor_2rooms ["201"].get_floor_stairs ()
        for key in self.floor_2stairs:
            door_coordinates = self.floor_2stairs [key]
            new_key = "floor2" + key
            self.add_floor2_room (new_key, door_coordinates [0], door_coordinates [1])

    #makes an object of a Floor2ClassRoom and adds the objects to a
    #dictionary of floor 2 rooms
    def add_floor2_room (self, room_name, row, col):
        floor_2_room = Floor2ClassRoom (row, col)
        self.floor_2rooms [room_name] = floor_2_room

    #makes an object of a Floor2ClassRoom and adds the objects to a
    #dictionary of floor 2 rooms
    def add_floor1_room (self, room_name, row, col):
        floor_1_room = Floor1ClassRoom (row, col)
        self.floor_1rooms [room_name] = floor_1_room

    #chooses map based on starting and ending rooms and returns a number
    #sets the floor, map and floor_dict
    #1 - both rooms in floor 1
    #2 - both rooms in floor 2
    #3 - start in floor 1, end in floor 2
    #4 - start in floor 2, end in floor 1
    def chooseMap (self, start, end):
        #checks which dictionary (floor1 or floor2 objects) the
        #starting rooms and ending rooms are in
        if (start in self.floor_1rooms):
            self.floor = 1
            self.map = self.floor_1rooms[start].get_floor_map()
            self.floor_dict = self.floor_1rooms
            if (end in self.floor_1rooms):
                return 1

            elif (end in self.floor_2rooms):
                return 3

        elif (start in self.floor_2rooms):
            self.floor = 2
            self.map = self.floor_2rooms[start].get_floor_map()
            self.floor_dict = self.floor_2rooms
            if (end in self.floor_2rooms):
                return 2
            
            if (end in self.floor_1rooms):
                return 4

    #given a room, this function finds the closest stairs, it
    #returns the name of that staircase and the path needed to get to
    #that staircase
    def find_closest_stairs(self, starting_room):
        stairs_dict = {}
        distances = []

        #finds the start
        if (self.floor == 1):
            stairs_dict = self.floor_1stairs
            start = "floor1"

        elif (self.floor == 2):
            stairs_dict = self.floor_2stairs
            start = "floor2"

        for key in stairs_dict:
            #in the classroom objects dictionaries, the keys for the stair cases
            #have the floor number in front
            new_key = start + key 
            path = self.findroute (starting_room, new_key)
            distances.append(path) #adds all the paths to each stairs to a list

        
        output = []

        #uses the first path as the shortest and iterates through the distances
        #list to find a path shorter than that
        path_chosen = distances[0]
        shortest = len(path_chosen)
        closest_stair = "stair" + "1"
        for i in range (5):
            if (distances [i] != None and len(distances[i]) < shortest):
                path_chosen = distances[i]
                shortest = len(path_chosen)
                closest_stair = "stair" + str(i + 1)

        #outputs path as well as stair name
        output = [closest_stair, path_chosen]
        return output


        
    def is_valid_move (self, row, col): # checks if the move is possible or not
        #0 means wall and the record has 30 rows and 30 total columns
        if (0 <= row < 30 and 0 <= col < 30 and self.map[row][col] != 0):
            return True

        else:
            return False
        
    def findroute (self, start, end): #start is the starting room number and end is
                                    #the ending room number
        #clears the path and visited set at the start of each findroute
        self.visited.clear()
        path = []

        #gets the row and column for the doors of each of the rooms given 
        start_room = self.floor_dict[start]
        start_row = start_room.get_doorRow()
        start_col = start_room.get_doorCol()
        end_room = self.floor_dict[end]
        end_row = end_room.get_doorRow()
        end_col = end_room.get_doorCol()

        #returns the path if found, otherwise, returns nothing
        if (self.dfs(start_row, start_col, end_row, end_col, path)):
            return path[ : :-1]  #returns the path in the reverse order, step is set to -1
        
        return None  # No path found
    

    def dfs(self, row, col, end_row, end_col, path):
        # base case: checks if destination is reached
        if ((row == end_row) and (col == end_col)):
            path.append((row, col)) #adds last cell to the path too
            return True
        
        # Mark current cell as visited or checked
        self.visited.add((row, col))
        
        # Possible directions to move: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for direction in directions:
            dr = direction [0]#row movement in direction
            dc = direction [1]#column movement in direction
            #row and column after direction movement
            new_row = row + dr
            new_col = col + dc
            
            #only visits the hallways and cells not already visited
            if ((self.is_valid_move(new_row, new_col)) and ((new_row, new_col) not in self.visited)):
                #end_row and end_col are kept same throughout
                if (self.dfs(new_row, new_col, end_row, end_col, path)):
                    #when a path till the ending room is found, each coordinate is added to path
                    path.append((row, col)) 
                    return True
        
        # If no path found, goes back by returning False
        return False

#testing class
if (__name__ == "__main__"):
    my_map = Map ()
    my_map.chooseMap("201", "203")
    print ("Path:", my_map.findroute("201", "203"))
    my_map.chooseMap("201", "115")
    print (my_map.find_closest_stairs ("201"))
    
    
