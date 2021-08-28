import pygame

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
    def __init__(self,x,y,width,height,name):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.rect = pygame.Rect(x,y,self.width,self.height)

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,colour):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x,y,self.width,self.height)  

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("ASSESTS/red.png")
        self.width,self.height = self.image.get_rect().size
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.velocity = 7
        
    def move(self,keys_pressed,room):
        if keys_pressed[pygame.K_a] and self.rect.x - self.velocity > room.left or keys_pressed[pygame.K_LEFT] and self.rect.x - self.velocity > room.left:  # LEFT
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.rect.x + self.velocity + self.width < room.right or keys_pressed[pygame.K_RIGHT] and self.rect.x + self.velocity + self.width < room.right:  # RIGHT
            self.rect.x += self.velocity
        if keys_pressed[pygame.K_w] and self.rect.y - self.velocity > room.top or keys_pressed[pygame.K_UP] and self.rect.y - self.velocity > room.top:  # UP
            self.rect.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.rect.y + self.velocity + self.height < room.bottom or  keys_pressed[pygame.K_DOWN] and self.rect.y + self.velocity + self.height < room.bottom:  # DOWN
            self.rect.y += self.velocity  
   
class Room():
    def __init__(self,name,image,doors,walls):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image)
        self.top = 200
        self.bottom = HEIGHT-10
        self.left = 13
        self.right = WIDTH - 13
        self.door_list = pygame.sprite.Group()
        
        for item in doors:
            door = Doors(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)

def room_change(player,room):
    """if player is colliding with door, move to the next room based on the .name of the door."""
    for door in room.door_list:
        if door.rect.colliderect(player.rect):
            if door.name == "1":
                new_room = room1
                if room == room2a: 
                    player.rect.x = spawn_x_right
                else:
                    player.rect.x,player.rect.y = spawn_x_center,spawn_y_center
            elif door.name == "1a":
                new_room = room1a
                if room == room1: 
                    player.rect.x,player.rect.y = spawn_x_center,spawn_y_bottom # moving player to spawn location of door in room
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
    return new_room
    
def draw_window(player,room):
    SCREEN.blit(room.image, (0,0))
    SCREEN.blit(player.image, (player.rect.x, player.rect.y))
    # for door in room.door_list: # un-code-comment to show doors
    #     pygame.draw.rect(SCREEN,(255,255,255),door.rect)
    pygame.display.update()

#rooms
room1 = Room("room1","backgrounds/BG-1.png",[[59,210,94,67,"1a"],[248,210,94,67,"1b"],[445,210,94,67,"1c"],[1060,0,40,650,"2a"]],[])
room1a = Room("room1a","backgrounds/BG-1-A.png",[[500,635,100,40,"1"]],[])        
room1b = Room("room1b","backgrounds/BG-1-B.png",[[500,635,100,40,"1"]],[])
room1c = Room("room1c","backgrounds/BG-1-C.png",[[500,635,100,40,"1"]],[])
room2a = Room("room2a","backgrounds/BG-2-A.png",[[0,0,40,650,"1"],[1060,0,40,650,"2b"]],[])
room2b = Room("room2b","backgrounds/BG-2-B.png",[[0,0,40,650,"2a"],[1060,0,40,650,"3"]],[])
room3  = Room("room3","backgrounds/BG-3.png",[[0,0,40,650,"2b"]],[])

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