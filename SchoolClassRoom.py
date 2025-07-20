#Program Name: SchoolClassRoom class for Porter Maps
#Program Authors: Safia Safia
#Date: January 15, 2025
#Program Description: This class is a base class that can be
#used to create an object of a room in the school. It has two
#getter methods that allow other programs to get the doorRow and
#doorCol of a room

class SchoolClassRoom():
    def __init__ (self, door_row, door_col):
        self.door_row = door_row
        self.door_col = door_col

    #getters
    def get_doorRow (self):
        return self.door_row

    def get_doorCol (self):
        return self.door_col


#testing class
if (__name__ == "__main__"):
    my_classroom = SchoolClassRoom (10, 4)
    print (my_classroom.get_doorRow())
    print (my_classroom.get_doorCol())


    
        



