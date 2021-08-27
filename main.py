import pygame

pygame.init()
pygame.display.set_caption("BOB the Blob")
scale = 0
WIDTH,HEIGHT = 1100,800-scale
BORDER_WIDTH,BORDER_HIGHT = WIDTH-10,HEIGHT-10

bg1 = pygame.image.load("backgrounds/BG-1.png")
bg1a = pygame.image.load("backgrounds/BG-1-A.png")
bg2 = pygame.image.load("backgrounds/BG-2-A.png")
bg3 = pygame.image.load("backgrounds/BG-3.png")


SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (140,140,200)

FPS = 60
VEL = 10


image = pygame.image.load("ASSESTS/square-48.png")



class Doors(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,name):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.rect = pygame.Rect(x,y,self.width,self.height)
        
        

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("ASSESTS/red.png")
        self.width,self.height = self.image.get_rect().size
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.velocity = 7
        self.house_spawn = (460,740)
        
    def move(self,keys_pressed,room):
        if keys_pressed[pygame.K_a] and self.rect.x - self.velocity > room.left or keys_pressed[pygame.K_LEFT] and self.rect.x - self.velocity > room.left:  # LEFT
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.rect.x + self.velocity + self.width < room.right or keys_pressed[pygame.K_RIGHT] and self.rect.x + self.velocity + self.width < room.right:  # RIGHT
            self.rect.x += self.velocity
        if keys_pressed[pygame.K_w] and self.rect.y - self.velocity > room.top or keys_pressed[pygame.K_UP] and self.rect.y - VEL > room.top:  # UP
            self.rect.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.rect.y + self.velocity + self.height < room.bottom or  keys_pressed[pygame.K_DOWN] and self.rect.y + self.velocity + self.height < room.bottom:  # DOWN
            self.rect.y += self.velocity  
 

    

# class Room():
#     def __init__(self,image,top,bottom,left,right):
#         super().__init__()
#         self.image = image
#         self.top = top + 10
#         self.bottom = bottom - 10
#         self.left = left + 10
#         self.right = right - 10
        
class Room1():
    def __init__(self):
        self.door_list = pygame.sprite.Group()
        self.bg_image = pygame.image.load("backgrounds/BG-1.png")
        self.top = 425
        self.bottom = HEIGHT -5
        self.left = 10
        self.right = WIDTH - 10
        
        doors = [[59,360,94,110,"1a"],
                 [248,360,94,110,"1b"],
                 [445,360,94,110,"1c"],
                 [1060,426,40,370,"2"]
                 ]
        
        # self.door1a = Doors(59,360,94,110,"door1a")
        # self.door1b = Doors(248,360,94,110,"door1b")
        # self.door1c = Doors(445,360,94,110,"door1c")
        # self.door2 = Doors(1060,426,40,370,"door2")
        
        for item in doors:
            door = Doors(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)

class Room1A():
    def __init__(self):
        self.door_list = pygame.sprite.Group()
        self.bg_image = pygame.image.load("backgrounds/BG-1-A.png")
        self.top = 40
        self.bottom = HEIGHT - 40
        self.left = 40
        self.right = WIDTH - 40
        
        doors = [[441,757,218,40,"1"]]
        for item in doors:
            door = Doors(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)

class Room1B():
    def __init__(self):
            self.door_list = pygame.sprite.Group()
            self.bg_image = pygame.image.load("backgrounds/BG-1-B.png")
            self.top = 40
            self.bottom = HEIGHT - 40
            self.left = 40
            self.right = WIDTH - 40
            
            doors = [[441,757,218,40,"1"]]
            for item in doors:
                door = Doors(item[0], item[1], item[2], item[3], item[4])
                self.door_list.add(door)

class Room1C():
    def __init__(self):
            self.door_list = pygame.sprite.Group()
            self.bg_image = pygame.image.load("backgrounds/BG-1-C.png")
            self.top = 40
            self.bottom = HEIGHT - 40
            self.left = 40
            self.right = WIDTH - 40
            
            doors = [[441,757,218,40,"1"]]
            for item in doors:
                door = Doors(item[0], item[1], item[2], item[3], item[4])
                self.door_list.add(door)
                
class Room2():
    def __init__(self):
        self.door_list = pygame.sprite.Group()
        self.bg_image = pygame.image.load("backgrounds/BG-2-A.png")
        self.top = 425
        self.bottom = HEIGHT -5
        self.left = 10
        self.right = WIDTH - 10
        
        doors = [[0,426,40,370,"1"],
                 [1060,426,40,370,"3"]
                 ]
        
        # self.door1a = Doors(59,360,94,110,"door1a")
        # self.door1b = Doors(248,360,94,110,"door1b")
        # self.door1c = Doors(445,360,94,110,"door1c")
        # self.door2 = Doors(1060,426,40,370,"door2")
        
        for item in doors:
            door = Doors(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)
            
class Room3():
    def __init__(self):
        self.door_list = pygame.sprite.Group()
        self.bg_image = pygame.image.load("backgrounds/BG-3.png")
        self.top = 425
        self.bottom = HEIGHT -5
        self.left = 10
        self.right = WIDTH - 10
        
        doors = [[0,426,40,370,"2"],
                 [1060,426,40,370,"4"]
                 ]
        
        # self.door1a = Doors(59,360,94,110,"door1a")
        # self.door1b = Doors(248,360,94,110,"door1b")
        # self.door1c = Doors(445,360,94,110,"door1c")
        # self.door2 = Doors(1060,426,40,370,"door2")
        
        for item in doors:
            door = Doors(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)


def room_change(player,room):
    """if player is colliding with door, move to the next room based on the .name of the door."""
    for door in room.door_list:
        if door.rect.colliderect(player.rect):
            if door.name == "1":
                new_room = Room1()
            elif door.name == "1a":
                new_room = Room1A()
                if room == Room1(): #moving from 
                    player.rect.x,player.rect.y = player.house_spawn # moving player to spawn location of door in room
            elif door.name == "1b":
                new_room = Room1B()
            elif door.name == "1c":
                new_room = Room1C()
            elif door.name == "2":
                new_room = Room2()
                if room == Room1(): # moving from left to right
                    player.rect.x = 50 # moving player to the left of screen without effecting the y
            elif door.name == "3":
                new_room == Room3()
            
        else:
            new_room = room
                
            
               
    return new_room
    
def draw_window(player, room,scale):
    
    SCREEN.blit(room.bg_image, (0,-scale))
    SCREEN.blit(player.image, (player.rect.x, player.rect.y-scale))
    for door in room.door_list:
        pygame.draw.rect(SCREEN,(255,255,255),door.rect)
        #SCREEN.blit(door.rect, (door.rect.x, door.rect.y-scale))
    pygame.display.update()

def main():
    
    player = Player(200,550)
    clock = pygame.time.Clock()
    room1 = Room1()
    room = room1
    #room1a = Room1A()
    room
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        player.move(keys_pressed,room)
        #door_hit_list = pygame.sprite.spritecollide(player,room.door_list, False)
    
        room = room_change(player, room)
        draw_window(player,room,scale)
        
    
if __name__ == "__main__":
    main()
