import pygame
import random

'''
This Code was made largely by myself, Oliver Waldock. In saying that 
I did use pieces of others work. If I have used others code I have refrenced
it with the code taken.
'''


pygame.init()
pygame.display.set_caption("BOB the Blob")

scale = -150
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
    def __init__(self,name,image,doors,border,walls):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image)
        self.top = border[0]
        self.bottom = border[1]
        self.left = border[2]
        self.right = border[3]
        self.door_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.walls = walls
        for item in doors:
            door = Doors(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)
        if walls != []:
            for item in walls:
                wall = Walls(item[0], item[1], item[2], item[3], item[4])
                self.wall_list.add(wall)

def generate_maze():
    maze = [
        ["T","-","-","-","-","-","-","-","-","-","-","-","-","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["l",".",".",".",".",".",".",".",".",".",".",".",".","l"],
        ["-","-","-","-","-","-","-","-","-","-","-","-","-","-"]]
    return maze


def create_maze():
    maze_grid = generate_maze()
    x_c = 84
    y_c = 71
    vertical = (10,71)
    horizontal = (84,10)
    dot = 10,10
    width = 14 
    height = 10
    walls = []
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
    print(walls)
    return walls


def room_change(player,room):
    """If player is colliding with door, move to the next room based on the .name of the door."""
    for door in room.door_list:
        if door.rect.colliderect(player.rect):
            if door.name == "1":
                new_room = room1
                if room == room2a: 
                    player.rect.x = spawn_x_right
                elif room == room1a:
                    player.rect.x,player.rect.y = 84,280
                elif room == room1b:
                    player.rect.x,player.rect.y = 273,280
                elif room == room1c:
                    player.rect.x,player.rect.y = 470,280
            elif door.name == "1a":
                new_room = room1a
                if room == room1: 
                    player.rect.x,player.rect.y = spawn_x_center,spawn_y_bottom
            elif door.name == "1b":
                new_room = room1b
                if room == room1: 
                    player.rect.x,player.rect.y = spawn_x_center,spawn_y_bottom
            elif door.name == "1c":
                new_room = room1c
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
                if room == room3:
                    player.rect.x,player.rect.y = spawn_x_right,spawn_y_center
    return new_room



def draw_window(player,room):
    '''Draws display on screen'''
    SCREEN.blit(room.image, (0,0))
    SCREEN.blit(player.image, (player.rect.x, player.rect.y))
    # for door in room.door_list: # un-code-comment to show doors
    #     pygame.draw.rect(SCREEN,(255,255,255),door.rect)
    if room.walls != []:
        for wall in room.wall_list:
            pygame.draw.rect(SCREEN,wall.colour,wall.rect)
    pygame.display.update()

s_border = (200,HEIGHT-5,5,WIDTH - 5)
f_border = (5,HEIGHT-5,5,WIDTH - 5)

#walls (roomname_ws) ws = walls

if random.randint(1,2) == 1:
    stopper_wall = [248,435,22,127,LEAVES]
else:
    stopper_wall = [248,540,22,127,LEAVES]
    
room2a_ws = [[450,294,650,22,LEAVES],[590,294,22,110,LEAVES],[1078,294,22,178,LEAVES],[681,382,336,22,LEAVES],[681,382,22,126,LEAVES],[450,487,253,22,LEAVES],[450,628,650,22,LEAVES],[750,472,22,178,LEAVES],[915,472,22,178,LEAVES],[832,382,22,180,LEAVES],[996,382,22,180,LEAVES],[996,543,104,22,LEAVES]]
room2b_ws = [[0,294,22,180,LEAVES],[0,294,291,22,LEAVES],[0,540,112,22,LEAVES],[0,628,1100,22,LEAVES],[90,382,22,180,LEAVES],[90,382,818,22,LEAVES],[270,228,830,22,LEAVES],[270,228,22,88,LEAVES],[179,460,296,22,LEAVES],[355,323,22,81,LEAVES],[441,305,553,22,LEAVES],[541,382,22,190,LEAVES],[270,460,22,103,LEAVES],[179,540,112,22,LEAVES],[179,540,22,100,LEAVES],[366,549,22,100,LEAVES],[453,549,22,109,LEAVES],[542,382,22,190,LEAVES],[542,552,102,22,LEAVES],[636,475,103,22,LEAVES],[717,382,22,268,LEAVES],[886,382,22,92,LEAVES],[808,464,22,98,LEAVES],[808,541,292,22,LEAVES],[972,305,22,257,LEAVES],[1078,229,22,230,LEAVES]]
room3_ws = [[0,229,22,228,LEAVES],[0,435,270,22,LEAVES],[0,540,270,22,LEAVES],[0,630,270,22,LEAVES],stopper_wall]
#rooms
room1 = Room("room1","backgrounds/BG-1.png",[[59,210,94,67,"1a"],[248,210,94,67,"1b"],[445,210,94,67,"1c"],[1085,0,15,650,"2a"]],s_border,[])
room1a = Room("room1a","backgrounds/BG-1-A.png",[[500,635,100,15,"1"]],s_border,[])        
room1b = Room("room1b","backgrounds/BG-1-B.png",[[500,635,100,15,"1"]],s_border,[])
room1c = Room("room1c","backgrounds/BG-1-C.png",[[500,635,100,15,"1"]],s_border,[])
room2a = Room("room2a","backgrounds/BG-2-A.png",[[0,0,15,650,"1"],[1085,0,15,650,"2b"]],s_border,room2a_ws)
room2b = Room("room2b","backgrounds/BG-2-B.png",[[0,0,15,650,"2a"],[1085,0,15,650,"3"]],s_border,room2b_ws)
room3  = Room("room3","backgrounds/BG-3.png",[[0,0,15,650,"2b"],[738,210,28,39,"4"]],s_border,room3_ws)
room4 = Room("room4","backgrounds/MAZE-BG.png",[[0,0,5,650,"3"]],f_border,create_maze())

spawn_x_left = 50
spawn_x_right = WIDTH - (100)
spawn_x_center = WIDTH/2
spawn_y_center = HEIGHT/2
spawn_y_bottom = HEIGHT - 120
    
player = Player(spawn_x_center,spawn_y_center)
clock = pygame.time.Clock()
room = room1
run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys_pressed = pygame.key.get_pressed()
    player.move(keys_pressed,room)
    #door_hit_list = pygame.sprite.spritecollide(player,room.door_list, False)
    for door in room.door_list:
        if door.rect.colliderect(player.rect):
            room = room_change(player, room)
    draw_window(player,room)