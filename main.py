#Program Name: PorterMap
#Program Authors: Anuva Nath, Sulagna Saha, Safia Safia
#Date: January 15, 2025
#Program Description: This program is a pygame application that gives the user the
#shortest path that they should take to get from one classroom to the next.
#It has a main menu page, a page for putting in the class room numbers, a page
#with the maps and a page with the route on the map.

import pygame
import sys

from Map import *
from Constants import *

pygame.init()

#displaying the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Porter Maps")

#common fonts being used
normal_font = pygame.font.Font("font.otf", 50)
font_textbox = pygame.font.Font("Font_textbox.otf", 20)

#home page - images
background_image1 = pygame.image.load("mainpage.png")  
background_image1 = pygame.transform.scale(background_image1,
                                           (SCREEN_WIDTH, SCREEN_HEIGHT))

#home page - buttons
start_button  = pygame.Rect ((SCREEN_WIDTH - BUTTON_WIDTH) // 2 - 30,
                             (SCREEN_HEIGHT - BUTTON_HEIGHT) // 2 + 200, BUTTON_WIDTH, BUTTON_HEIGHT)

exit_button = pygame.Rect (SCREEN_WIDTH - 70,
                             10, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)

#floor selector page - images
background2 = pygame.image.load("background2.png")  
background2 = pygame.transform.scale(background2, (SCREEN_WIDTH, SCREEN_HEIGHT))

#floor selector page - buttons
button_floor1 = pygame.Rect (100, 470, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT)
button_floor2 = pygame.Rect (440, 470, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT)

#boxes for the user to type in room numbers
input_box1 = pygame.Rect(240, 260, 320, 40)
input_box2 = pygame.Rect(240, 420, 320, 40)

#floor_map page and floor display page - images
start_point = pygame.image.load("start.png")
start_point = pygame.transform.scale(start_point, (20, 20))

end_point = pygame.image.load("destination.png")
end_point = pygame.transform.scale(end_point, (385 / 20, 512 / 20))

floor1_img = pygame.image.load("floor1.png").convert()
floor1_img = pygame.transform.scale(floor1_img, (800, 600))

floor2_img = pygame.image.load("floor2.png").convert()
floor2_img = pygame.transform.scale(floor2_img, (800, 600))

#floor_map page and floor display page - buttons
back_button = pygame.Rect (625, 450, BUTTON_WIDTH - 50, BUTTON_HEIGHT)
next_floor = pygame.Rect (625, 350, BUTTON_WIDTH - 50, BUTTON_HEIGHT)



# function for adding text to the screen
def draw_text(text, font, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))
    
#function for closing the screen
def close_application ():
    pygame.quit()
    sys.exit()

    
# Startup page - allows user to either start the application and close it
def startup_page():
    #Background music
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(0.5)  
    pygame.mixer.music.play (-1, start = 5) #loops the song infinitely,
    #song starts 5 seconds into the song file, by doing start = 5, we
    #ensure the user can hear the song the moment they start this application
        
    running = True
    while (running):
        screen.blit (background_image1, (0, 0))  

        #Start Button
        pygame.draw.rect (screen, BLUE, start_button)
        draw_text ("START", normal_font, WHITE, start_button.left + 37,
                   start_button.top + 20)


        #Exit Button
        pygame.draw.rect (screen, RED, exit_button)
        draw_text ("X", normal_font, BLACK, exit_button.left + 15,
                   exit_button.top)
        
        for event in pygame.event.get():
            #user closed the pygame tab
            if (event.type == pygame.QUIT):
                close_application ()

            #user clicked with mouse
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (start_button.collidepoint(event.pos)):
                    running = False

                elif (exit_button.collidepoint(event.pos)):
                    close_application ()
                    
        pygame.display.flip()

# Floor selector page (user selects Floor 1 or Floor 2)
def floor_selector_page(start_song = True):
    #makes sure the song doen't restart when the user comes back to the floor
    #selector page
    if (start_song): 
        pygame.mixer.music.unload () #unloads the last song file
        pygame.mixer.music.load ("Dora the explorer (Im the map).mp3")  
        pygame.mixer.music.set_volume (0.5)
        pygame.mixer.music.play (-1) #loops the song

    text1 = "" #text received from user for starting classroom
    text2 = "" #text received from user for destination classroom

    #boolean for checking which of the two user_input boxes are active or clicked on
    active_box1 = False
    active_box2 = False

    running = True
    
    while (running):
        #background
        screen.blit(background2, (0, 0))

        # Buttons for Floor Maps
        pygame.draw.rect(screen, BLUE, button_floor1)
        pygame.draw.rect(screen, GREEN, button_floor2)
        draw_text("Floor 1 Map", normal_font, WHITE, 125, 480)
        draw_text("Floor 2 Map", normal_font, WHITE, 455, 480)

        #Text input boxes
        #outline of rectangle for input boxes becomes black when clicked on and
        #grey otherwise
        colour1 = GRAY
        colour2 = GRAY
        
        if (active_box1):
            colour1 = BLACK
            
        elif (active_box2):
            colour2 = BLACK

        pygame.draw.rect(screen, colour1, input_box1, 2) 
        pygame.draw.rect(screen, colour2, input_box2, 2)
        # 2 is border thickness, colour1 is the border colour

        #draws the text that user enters as starting room number and ending room
        #number onto the screen
        draw_text (text1, font_textbox, BLACK, input_box1.x + 3, input_box1.y + 5)
        draw_text (text2, font_textbox, BLACK, input_box2.x + 3, input_box2.y + 5)

        #goes through possible events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): #user closes the application
                close_application()

            if (event.type == pygame.MOUSEBUTTONDOWN): #mouse pressed
                #checks which active box is clicked on or which button is pressed
                if (input_box1.collidepoint(event.pos)):
                    active_box1 = True
                    active_box2 = False

                elif (input_box2.collidepoint(event.pos)):
                    active_box2 = True
                    active_box1 = False
                    
                else:
                    active_box1 = False
                    active_box2 = False
                    #buttons
                    if (button_floor1.collidepoint(event.pos)):
                        running = False
                        floor_map (1)  # floor map of floor 1

                    elif (button_floor2.collidepoint(event.pos)):
                        running = False
                        floor_map (2)  # floor map of floor 2

            if (event.type == pygame.KEYDOWN): #user is typing
                if (active_box1 or active_box2): #user is typing in the text input boxes
                    #enter makes user input box inactive
                    if (event.key == pygame.K_RETURN):
                        if (active_box1):
                            active_box1 = False
                            
                        else:
                            active_box2 = False

                    #backspace removes letters user already typed
                    elif (event.key == pygame.K_BACKSPACE):
                        if (active_box1):
                            text1 = text1[: -1] #removes last letter
                
                        else:
                            text2 = text2[: -1]

                    #all other letters get added to the text
                    else:
                        if (active_box1):
                            text1 += event.unicode #receives the unicode for typed letter
                            
                        else:
                            text2 += event.unicode

                if ((event.key == pygame.K_RETURN) and (text1.strip()) and (text2.strip())):
                    #text1.strip() would return True if the text string is not empty and 
                    #false otherwise
                    floor_display (text1, text2) #text1  - start room, text2 - end room
                    running = False

        pygame.display.flip()


# Display floor map, allows the user to go back to floor selector page
def floor_map(floor):
    running = True
    
    while (running):
        # Display background image based on floor choice
        if (floor == 1):
            screen.blit (floor1_img, (0, 0))
        elif (floor == 2):
            screen.blit (floor2_img, (0, 0))

        #adds button
        pygame.draw.rect (screen, BLUE, back_button)
        draw_text ("BACK", normal_font, WHITE, back_button.left + 20, back_button.top + 20)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT): 
                close_application ()
                
            elif (event.type == pygame.MOUSEBUTTONDOWN): 
                if (back_button.collidepoint(event.pos)):
                    floor_selector_page (False)

        pygame.display.flip()


# Display floor images with the path the user needs to take on them,
#allows the user to go back to the floor selector page
def floor_display (starting_room, ending_room):
    running = True
    my_map = Map ()
    change_map = False
    floor_img = floor1_img
    
    while (running):
        # Display image based on starting_room choice
        map_chosen = my_map.chooseMap (starting_room, ending_room)

        if (change_map == False):
            if ((map_chosen == 1) or (map_chosen == 2)): 
                path = my_map.findroute(starting_room, ending_room)
                if (map_chosen == 1): #both rooms are on floor1
                    floor_img = floor1_img

                else: #both rooms are on floor2
                    floor_img = floor2_img

            elif ((map_chosen == 3) or (map_chosen == 4)):
                if (map_chosen == 3): #starting room is on floor1, ending room is on floor2
                    floor_img = floor1_img
                    start = "floor2"

                else: #starting room is on floor2, ending room is on floor1
                    floor_img = floor2_img
                    start = "floor1"

                old_ending_room = ending_room
                ending_room_info = my_map.find_closest_stairs(starting_room)
                ending_room = start + ending_room_info[0]
                path = ending_room_info[1]
                change_map = True

        #sets background of the screen
        screen.blit(floor_img, (0, 0))

        #button
        pygame.draw.rect(screen, BLUE, back_button)
        draw_text("BACK", normal_font, WHITE, back_button.left + 20, back_button.top + 20)

        #draw rectangles on the squares on the grid where the path is
        for coordinates in path:
            pygame.draw.rect(screen, DARK_GREEN, pygame.Rect( coordinates[1] * 20 + 5,
                                                                  coordinates[0] * 20 + 5, 10, 10))

        #draws symbols on the starting and ending positions
        start = path[0]
        end = path[-1]
            
        screen.blit(start_point,(start[1] * 20, start[0] * 20))
        screen.blit(end_point, (end[1] * 20, end[0] * 20 - 15))

        #adds next floor button if map needs to go from one floor to next
        if (change_map):
            pygame.draw.rect(screen, BLUE, next_floor)
            draw_text("Next", normal_font, WHITE, next_floor.left + 20, next_floor.top)
            draw_text("Floor", normal_font, WHITE, next_floor.left + 20, next_floor.top + 40)
            
        # Possible events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): #user closes application
                close_application ()
                
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (back_button.collidepoint(event.pos)): 
                    floor_selector_page(False)

                #only checks for next floor button if map is set to change
                elif ((change_map) and (next_floor.collidepoint(event.pos))): 
                    floor_display (ending_room, old_ending_room)

        pygame.display.flip()

def main ():
    startup_page()
    floor_selector_page()


main()
