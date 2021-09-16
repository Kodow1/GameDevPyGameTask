'''
This Code was made largely by myself, Oliver Waldock. In saying that 
I did use pieces of others work. If I have used others code I have refrenced
it with the code taken.

Music copyright disclaimer:
In my dreams - Fato Shadow
Paradise - Fato Shadow
bossfight - public domain
triamphant - public domain
'''

import pygame
import random
import time

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("BOB the Blob")

#Screen
WIDTH,HEIGHT = 1100,650
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60

#Colours
TRUNK = (231,185,133)
LEAVES = (140,197,128)
SKY = (180,219,248)
GRASS = (160,217,148)
WATER = (186,206,243)
WHITE = (255,255,255)
D_GREY = (100,100,100)
BLACK = (0,0,0)

class Doors(pygame.sprite.Sprite):
    '''Doors are created and used to move the player to adjacent rooms. 
    Which room is defined by self.name.
    Doors are not printed on screen'''
    def __init__(self,x,y,width,height,name):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.rect = pygame.Rect(x,y,self.width,self.height)

class Walls(pygame.sprite.Sprite):
    '''Walls are created and used to create a barrier that the player collieds with. Walls are visable.'''
    def __init__(self,x,y,width,height,colour):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x,y,self.width,self.height)
        
class Interactable(pygame.sprite.Sprite):
    """Interactables are sprites that the player can interacte with (NPC's and Buttons)"""
    def __init__(self,name,x,y,image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.name = name
        self.width,self.height = self.image.get_rect().size
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.react_rect = pygame.Rect(x-100,y-100,self.width+200,self.height+200)
        pass

class Player(pygame.sprite.Sprite):
    '''Creates a moveable sprite that is moved by keyboard inputs'''
    def __init__(self,x,y):
        self.image = pygame.image.load("ASSESTS/red.png")
        self.width,self.height = self.image.get_rect().size
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.velocity = 7
        self.change_x = 0
        self.change_y = 0
        self.rect_vel = pygame.Rect(x-self.velocity,y-self.velocity,self.width+(self.velocity*2),self.height+(self.velocity*2))
        
    def move(self,keys_pressed,room):
        '''Moves the player and check for collisions with the borders of the room and walls in the room
        Simpson Collagem Computer Scinece - Mazerunner (some collision elements with walls)'''
        if keys_pressed[pygame.K_a] and self.rect.x - self.velocity > room.left or keys_pressed[pygame.K_LEFT] and self.rect.x - self.velocity > room.left:  # LEFT
            self.change_x = (-1*self.velocity)
        if keys_pressed[pygame.K_d] and self.rect.x + self.velocity + self.width < room.right or keys_pressed[pygame.K_RIGHT] and self.rect.x + self.velocity + self.width < room.right:  # RIGHT
            self.change_x = self.velocity
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, room.wall_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        
        if keys_pressed[pygame.K_w] and self.rect.y - self.velocity > room.top or keys_pressed[pygame.K_UP] and self.rect.y - self.velocity > room.top:  # UP
            self.change_y = (-1*self.velocity)
        if keys_pressed[pygame.K_s] and self.rect.y + self.velocity + self.height < room.bottom or  keys_pressed[pygame.K_DOWN] and self.rect.y + self.velocity + self.height < room.bottom:  # DOWN
            self.change_y = self.velocity  
        self.rect.y += self.change_y    
        block_hit_list = pygame.sprite.spritecollide(self, room.wall_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        self.change_x = 0
        self.change_y = 0

class Room():
    '''Creates a room, stores doors and walls'''
    def __init__(self,name,image,doors,border,walls,interactables):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image)
        self.top = border[0]
        self.bottom = border[1]
        self.left = border[2]
        self.right = border[3]
        self.door_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.inter_list = pygame.sprite.Group()
        self.walls = walls
        for item in doors:
            door = Doors(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)
        if walls != []:
            for item in walls:
                wall = Walls(item[0], item[1], item[2], item[3], item[4])
                self.wall_list.add(wall)
        if interactables != []:
            for item in interactables:
                interactables = Interactable(item[0], item[1], item[2], item[3])
                self.inter_list.add(interactables)    

class HealthBar():
    """Creates a health bar displayed on the top right"""
    def __init__(self):
        self.health = 0
        self.images = [pygame.image.load("ASSESTS/Health-100.png"),pygame.image.load("ASSESTS/Health-50.png"),pygame.image.load("ASSESTS/Health-0.png")]

maze_liabry = {1:[
    #  x  0   1   2   3   4   5   6   7   8   9   10  11  12  13    y
        ["T","-","T","T","-","T","-","-","T","-","T","T","-","l"], #0
        ["T",".","l",".","T","-","-",".",".","l","l","-",".","l"], #1
        ["l","l","-","l","-","l","-","-","T","-","-","-",".","l"], #2
        ["l","T",".","T",".",".","T","l","-",".","-","l","-","l"], #3
        ["T","-","l","-","-","-","l","T",".","l","T","-","l","l"], #4
        ["T",".","-","T","-",".",".","-","l","-",".","T","T","l"], #5
        ["l","l","-",".","-","T",".","l","-","-",".",".",".","l"], #6
        ["T","-",".","T","l","l","-","l","-","l","l","l","-","l"], #7
        ["l","T",".",".","T",".","l","-","l","T",".","-","l","."], #8  
        ["-","-","-","-","-","-","-","-","-","-","-","-","-","-"]], #9
               2:[
    #  x  0   1   2   3   4   5   6   7   8   9   10  11  12  13    y
        ["T","T","-","-","T","-","-","-","-","T","-","-","-","l"], #0
        ["l","l","T","-","l","-","-","T","l",".","l","-","l","l"], #1
        ["l",".",".","l","l","T","-","l","-","T","-","l","l","l"], #2
        ["T","-","-",".","l","l","l",".","l","l","l","l","l","l"], #3
        ["l","l","-","T",".","l","-","l","l",".","l","-","l","l"], #4
        ["T","T",".","l","-","T",".","-","T","-","-",".","l","l"], #5
        ["l",".","-",".","l","l","-","-","-","l","-","T","l","l"], #6
        ["l","-","T","-",".","T","-","l","T","-",".","l",".","l"], #7
        ["T",".","l","-","-",".","l",".","-","l","-","-","-","."], #8
        ["-","-","-","-","-","-","-","-","-","-","-","-","-","l"]], #9
               3:[
    #  x  0   1   2   3   4   5   6   7   8   9   10  11  12  13    y
        ["T","-","-","-","-","-","T","-","T","T","-","-","T","l"], #0
        ["T","-","l","T","-","l","T",".","l","l","T",".","l","l"], #1
        ["l","l",".","l","l","l",".","l","l",".","l","l",".","l"], #2
        ["T","-",".","l","l","-","-",".","l","T",".","T","-","l"], #3
        ["l","-","-","l","l","-","-","-",".","T","-",".","l","l"], #4
        ["l","-","l","l","-","-","-","-","T",".","T","T",".","l"], #5
        ["T",".","l","T","-","T","-","l",".","T",".","l","-","l"], #6
        ["T","T",".",".","l",".","l","l","-",".","T","-","l","l"], #7
        ["l",".","T","-",".","T",".","l","-","-","-",".","l","."], #8
        ["-","-","-","-","-","-","-","-","-","-","-","-","-","-"]] #9
               }    

def create_maze(maze_num):
    """Turns mazes from maze liabry into a list of walls"""
    x_c = 84
    y_c = 71
    vertical = (10,71)
    horizontal = (84,10)
    dot = 10,10
    width = 14 
    height = 10
    walls = []
    maze_grid = maze_liabry[maze_num] 
    for x in range(0,width):
        for y in range(0,height):
            if maze_grid[y][x] == ".":
                walls.append([x*x_c,y*y_c,dot[0],dot[1],BLACK])
            elif maze_grid[y][x] == "-":
                walls.append([x*x_c,y*y_c,horizontal[0],horizontal[1],BLACK])
            elif maze_grid[y][x] == "l":
                walls.append([x*x_c,y*y_c,vertical[0],vertical[1],BLACK])
            elif maze_grid[y][x] == "T":
                walls.append([x*x_c,y*y_c,horizontal[0],horizontal[1],BLACK])
                walls.append([x*x_c,y*y_c,vertical[0],vertical[1],BLACK])
    return walls

def room_change(player,room):
    """If player is colliding with door, move to the next room based on the .name of the door."""
    for door in room.door_list:
        if door.rect.colliderect(player.rect):
            if door.name == "1":
                new_room = room1
                if room == house1:
                    player.rect.x,player.rect.y = 84,280
                elif room == house2:
                    player.rect.x,player.rect.y = 273,280
                elif room == house3:
                    player.rect.x,player.rect.y = 470,280
                elif room == room5:
                    player.rect.x = spawn_x_center
                else:
                    player.rect.x = spawn_x_right
            elif door.name == "1a":
                new_room = house1
                if room == room1: 
                    player.rect.x,player.rect.y = spawn_x_center,spawn_y_bottom
            elif door.name == "1b":
                new_room = house2
                if room == room1: 
                    player.rect.x,player.rect.y = spawn_x_center,spawn_y_bottom
            elif door.name == "1c":
                new_room = house3
                if room == room1: 
                    player.rect.x,player.rect.y = spawn_x_center,spawn_y_bottom
            elif door.name == "2a":
                new_room = room2a
                if room == room1: 
                    player.rect.x = spawn_x_left 
                elif room == room2b:
                    player.rect.x = spawn_x_right 
            elif door.name == "2b":
                new_room = room2b
                if room == room2a: 
                    player.rect.x = spawn_x_left 
                elif room == room3:
                    player.rect.x = spawn_x_right 
            elif door.name == "3":
                new_room = room3
                if room == room2b: 
                    player.rect.x = spawn_x_left 
            elif door.name == "4":
                new_room = room4
                chill.fadeout(50)
                boss.play(loops=100, maxtime=0, fade_ms=50)
                if room == room3:
                    player.rect.x,player.rect.y = spawn_x_left,spawn_y_top
            elif door.name == "5":
                new_room = room5
                boss.fadeout(50)
                triumphant.play(loops=100, maxtime=0, fade_ms=50)
                player.rect.x,player.rect.y = spawn_x_left,spawn_y_center
            elif door.name == "endscreen":
                new_room = endscreen
    return new_room

def draw_window(player,room):
    '''Draws display on screen'''
    SCREEN.blit(room.image, (0,0))
    # if room != homescreen or room != endscreen:
    #     SCREEN.blit(player.image, (player.rect.x, player.rect.y))
    SCREEN.blit(player.image, (player.rect.x, player.rect.y))
    if dialog_tally > 0:
        SCREEN.blit(health_bar.images[health_bar.health], (825, 16))
    for NPC in room.inter_list:
        SCREEN.blit(NPC.image, (NPC.rect.x, NPC.rect.y))
    # for door in room.door_list: # un-code-comment to show doors
    #     pygame.draw.rect(SCREEN,(255,255,255),door.rect)
    if room.walls != []:
        for wall in room.wall_list:
            pygame.draw.rect(SCREEN,wall.colour,wall.rect)
    pygame.display.update()

def dialog(d_t,interactable,room):
    """This finds what dialog needs to be asscess depending on how are the player has played which is kept track by dialog_tally or d_t"""
    in_dialog = True
    if interactable.name == "flower":
        list = ["ASSESTS/flower-1.png"]
        room.inter_list.remove(interactable)
        health_bar.health = 2
    elif interactable.name == "petal":
        list = ["ASSESTS/petal-1.png"]
        room.inter_list.remove(interactable)
        health_bar.health = 1
    elif d_t == 0:
        if interactable.name =="Cole":
            list = ["ASSESTS/1-0.png"]
        else:
            list = ["ASSESTS/0-0.png","ASSESTS/0-1.png","ASSESTS/0-2.png","ASSESTS/0-3.png"]
            d_t +=1
    elif d_t == 1:
        if interactable.name =="Cole":
            list = ["ASSESTS/1-0.png","ASSESTS/1-1.png","ASSESTS/1-2.png","ASSESTS/1-3.png","ASSESTS/1-4.png","ASSESTS/1-5.png","ASSESTS/1-6.png","ASSESTS/1-7.png","ASSESTS/1-8.png","ASSESTS/1-9.png","ASSESTS/1-10.png"]
            d_t +=1
        elif interactable.name == "Mr.Blue":
            list = ["ASSESTS/0-1.png"]
        else:
            list = ["ASSESTS/p-1.png"]
    else:
        if interactable.name =="Cole":
            list = ["ASSESTS/c-2.png"]
        elif interactable.name == "Mr.Blue":
            list = ["ASSESTS/0-1.png"]
        else:
            list = ["ASSESTS/p-2.png"]
    return in_dialog,list,d_t 

if True: # Stores all base varibales in a collapsible state
    s_border = (200,HEIGHT-5,5,WIDTH - 5)
    f_border = (3,HEIGHT-3,3,WIDTH - 3)


    #walls (roomname_ws) ws = walls

    if random.randint(1,2) == 1:
        stopper_wall = [248,435,22,127,LEAVES]
    else:
        stopper_wall = [248,540,22,127,LEAVES]


    room2a_ws = [[590,294,510,22,LEAVES],[590,294,22,110,LEAVES],[1078,294,22,178,LEAVES],[681,382,336,22,LEAVES],[681,382,22,126,LEAVES],[450,487,253,22,LEAVES],[450,628,650,22,LEAVES],[750,472,22,178,LEAVES],[915,472,22,178,LEAVES],[832,382,22,180,LEAVES],[996,382,22,180,LEAVES],[996,543,104,22,LEAVES]]
    room2b_ws = [[0,294,22,180,LEAVES],[0,294,291,22,LEAVES],[0,540,112,22,LEAVES],[0,628,1100,22,LEAVES],[90,382,22,180,LEAVES],[90,382,818,22,LEAVES],[270,228,830,22,LEAVES],[270,228,22,88,LEAVES],[179,460,296,22,LEAVES],[355,323,22,81,LEAVES],[441,305,553,22,LEAVES],[541,382,22,190,LEAVES],[270,460,22,103,LEAVES],[179,540,112,22,LEAVES],[179,540,22,100,LEAVES],[366,549,22,100,LEAVES],[453,549,22,109,LEAVES],[542,382,22,190,LEAVES],[542,552,102,22,LEAVES],[636,475,103,22,LEAVES],[717,382,22,268,LEAVES],[886,382,22,92,LEAVES],[808,464,22,98,LEAVES],[808,541,292,22,LEAVES],[972,305,22,257,LEAVES],[1078,229,22,230,LEAVES]]
    room3_ws = [[0,229,22,228,LEAVES],[0,435,270,22,LEAVES],[0,540,270,22,LEAVES],[0,630,270,22,LEAVES],stopper_wall]

    #buttons
    start_buttons = [["easy",430,215,"ASSESTS/240x70.png"],["medium",430,316,"ASSESTS/240x70.png"],["hard",430,417,"ASSESTS/240x70.png"]]
    end_buttons = [["play_again",296,458,"ASSESTS/240x70.png"],["quit",569,458,"ASSESTS/240x70.png"]]
    
    # NPC's
    house1_npcs = [["Cole",230,300,"ASSESTS/yellow.png"]]
    house2_npcs = [["Folyd",300,300,"ASSESTS/pink.png"],["Mr. Blue",230,300,"ASSESTS/blue-100.png"]]
     
    #flower
    flower =[["flower",(WIDTH/2)-55,(HEIGHT/2)-107,"ASSESTS/Flower.png"]]
    petal =[["petal",WIDTH/2,HEIGHT/2,"ASSESTS/Petal.png"]]
    
    #rooms
    homescreen = Room("homescreen","backgrounds/homescreen.png",[],f_border,[],start_buttons)
    room1 = Room("room1","backgrounds/BG-1.png",[[59,210,94,67,"1a"],[248,210,94,67,"1b"],[445,210,94,67,"1c"],[1085,0,15,650,"2a"]],s_border,[],[])
    house1 = Room("house1","backgrounds/BG-house.png",[[500,635,100,15,"1"]],s_border,[],house1_npcs)        
    house2 = Room("house2","backgrounds/BG-house.png",[[500,635,100,15,"1"]],s_border,[],house2_npcs)
    house3 = Room("house3","backgrounds/BG-house.png",[[500,635,100,15,"1"]],s_border,[],[])
    room2a = Room("room2a","backgrounds/BG-2-A.png",[[0,0,15,650,"1"],[1085,0,15,650,"2b"]],s_border,room2a_ws,[])
    room2b = Room("room2b","backgrounds/BG-2-B.png",[[0,0,15,650,"2a"],[1085,0,15,650,"3"]],s_border,room2b_ws,[])
    room3  = Room("room3","backgrounds/BG-3.png",[[0,0,15,650,"2b"],[738,210,28,39,"4"]],s_border,room3_ws,petal)
    # room 4 is in main loop
    room5 = Room("room5","backgrounds/Final-BG.png",[[1085,0,15,650,"endscreen"]],f_border,[],flower)
    endscreen = Room("endscreen","backgrounds/Asset 40.png",[],f_border,[],end_buttons)
    
    #spawn numbers =
    spawn_x_left = 50
    spawn_x_right = WIDTH - (100)
    spawn_x_center = WIDTH/2
    spawn_y_center = HEIGHT/2
    spawn_y_bottom = HEIGHT - 120
    spawn_y_top = 20
    
    #Sound
    boss = pygame.mixer.Sound("Music/bossfight.wav")
    triumphant = pygame.mixer.Sound("Music/triumphant.wav")
    chill1 = pygame.mixer.Sound("Music/fato_shadow_-_in_my_dreams.wav")
    chill2 = pygame.mixer.Sound("Music/fato_shadow_-_paradise.wav")
    if random.randint(1,2) == 1:
        chill = chill1
    else:
        chill = chill2
    chill.set_volume(0.5)
    boss.set_volume(0.5)
    triumphant.set_volume(0.7)
    chill.play(loops=30, maxtime=0, fade_ms=0)
    
    #Other
    health_bar = HealthBar()
    clock = pygame.time.Clock()
    room = homescreen
    run = True
    player = Player(spawn_x_center,spawn_y_center)
    dialog_tally = 0
    in_dialog = False

while run:
    clock.tick(FPS)
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if room == homescreen: # Homescreen programing
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed(num_buttons=3)
        for button in room.inter_list:
            if button.rect.collidepoint(mouse_pos) == True and mouse_pressed[0] == True:
                room = room1
                if button.name == "hard":
                    maze_num = 3
                elif button.name == "medium":
                    maze_num = 2
                elif button.name == "easy":
                    maze_num = 1
                room4 = Room("room4","backgrounds/MAZE-BG.png",[[0,0,5,650,"3"],[1090,620,10,30,"5"]],f_border,create_maze(maze_num),[])
        SCREEN.blit(room.image, (0,0))
        pygame.display.update()
    elif room == endscreen: # Endscreen programing w/ reset if "play again"
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed(num_buttons=3)
        for button in room.inter_list:
            if button.rect.collidepoint(mouse_pos) == True and mouse_pressed[0] == True:
                if button.name == "play_again":
                    room = homescreen
                    dialog_tally = 0
                    health_bar.health = 0
                    player = Player(spawn_x_center,spawn_y_center)
                    room3  = Room("room3","backgrounds/BG-3.png",[[0,0,15,650,"2b"],[738,210,28,39,"4"]],s_border,room3_ws,petal)
                    room5 = Room("room5","backgrounds/Final-BG.png",[[1085,0,15,650,"endscreen"]],f_border,[],flower)  
                    if random.randint(1,2) == 1:
                        chill = chill1
                    else:
                        chill = chill2
                    chill.play(loops=30, maxtime=0, fade_ms=0)
                    triumphant.stop()
                else:
                    run = False
        SCREEN.blit(room.image, (0,0))
        pygame.display.update() 
    else:
        keys_pressed = pygame.key.get_pressed()
        if in_dialog == False: #Check to start dialog
            if keys_pressed[pygame.K_SPACE]==True:
                for NPC in room.inter_list:
                    if NPC.react_rect.colliderect(player.rect):
                        in_dialog,list,dialog_tally = dialog(dialog_tally,NPC,room)
                        counter = -1
                        break
            #player movement
            player.move(keys_pressed,room)
            for door in room.door_list:
                if door.rect.colliderect(player.rect):
                    room = room_change(player, room)
            draw_window(player,room)
        else: # is in dialog
            length = len(list)-1
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]==True:
                if counter<=(length-1): 
                    counter += 1
                    SCREEN.blit(pygame.image.load(list[counter]),(0,500))
                    pygame.display.update()
                    time.sleep(1)
                else:
                    in_dialog = False
                    time.sleep(0.3)