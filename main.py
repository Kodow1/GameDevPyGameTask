import pygame

pygame.init()
pygame.display.set_caption("BOB the Blob")

WIDTH,HEIGHT = 1100,650
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
        self.surface = pygame.Surface([width,height])
        self.rect = self.surface.get_rect()
        

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("ASSESTS/red.png")
        self.width,self.height = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.velocity = 7
        
    def move(self,keys_pressed,room):
        if keys_pressed[pygame.K_a] and self.x - self.velocity > room.left or keys_pressed[pygame.K_LEFT] and self.x - self.velocity > room.left:  # LEFT
            self.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.x + self.velocity + self.width < room.right or keys_pressed[pygame.K_RIGHT] and self.x + self.velocity + self.width < room.right:  # RIGHT
            self.x += self.velocity
        if keys_pressed[pygame.K_w] and self.y - self.velocity > room.top or keys_pressed[pygame.K_UP] and self.y - VEL > room.top:  # UP
            self.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.y + self.velocity + self.height < room.bottom or  keys_pressed[pygame.K_DOWN] and self.y + self.velocity + self.height < room.bottom:  # DOWN
            self.y += self.velocity  
 
def room_change(player,room):
    """if player is colliding with door, move to the next room based on the .name of the door."""
    for door in room.door_list:
        if door.rect.colliderect(player.rect):
            print (door.name)
    

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
        self.bottom = HEIGHT - 10
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



# class Room1A():
#     def __init__(self):
#         self.door_list = pygame.sprite.Group()
#         self.bg_image = pygame.image.load("backgrounds/BG-1-A.png")
#         self.top = 40
#         self.bottom = HEIGHT - 40
#         self.left = 40
#         self.right = WIDTH - 40
        
#         doors = [[248,360,94,110]]
#         for item in doors:
#             door = Doors(item[0], item[1], item[2], item[3])
#             self.door_list.add(door)


        
def draw_window(player, room,scale):
    SCREEN.blit(room.bg_image, (0,-scale))
    SCREEN.blit(player.image, (player.x, player.y-scale))
    for door in room.door_list:
        SCREEN.blit(door.surface, (door.x, door.y-scale))
    pygame.display.update()

def main():
    
    scale = 150
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
    
        room_change(player, room)
        draw_window(player,room,scale)
    
if __name__ == "__main__":
    main()
