import pygame

pygame.init()
pygame.display.set_caption("{Enter title here.}")

WIDTH,HEIGHT = 1200,1000

BORDER = pygame.Rect(10,10,WIDTH-10,HEIGHT-10)


BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (140,140,200)

FPS = 60


VEL = 10

#PLAYER set up
PLAYER_WIDTH,PLAYER_HEIGHT = 48,48
PLAYER_IMAGE = pygame.image.load("ASSESTS/square-48.png")

#ENERMY set up
ENERMY_WIDTH,ENERMY_HEIGHT = 48,48
ENERMY_IMAGE = pygame.image.load("ASSESTS/square-48.png")

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))





def draw_window(player,enermy):
    SCREEN.fill(BLUE)
    SCREEN.blit(PLAYER_IMAGE, (player.x, player.y))
    SCREEN.blit(ENERMY_IMAGE, (enermy.x, enermy.y))
         
    pygame.display.update()

def player_handle_movement(keys_pressed,player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0 or keys_pressed[pygame.K_LEFT] and player.x - VEL > 0:  # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x + VEL + PLAYER_WIDTH < BORDER.width or keys_pressed[pygame.K_RIGHT] and player.x + VEL + PLAYER_WIDTH < BORDER.width:  # RIGHT
        player.x += VEL 
    if keys_pressed[pygame.K_w] and player.y - VEL > 0 or keys_pressed[pygame.K_UP] and player.y - VEL > 0:  # UP
        player.y -= VEL
    if keys_pressed[pygame.K_s] and player.y + VEL + PLAYER_HEIGHT < BORDER.height or  keys_pressed[pygame.K_DOWN] and player.y + VEL + PLAYER_HEIGHT < BORDER.height:  # DOWN
        player.y += VEL


#Main Loop
def main():
    player = pygame.Rect(700,300,PLAYER_WIDTH,PLAYER_HEIGHT)
    enermy = pygame.Rect(500,300,ENERMY_WIDTH,ENERMY_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player)        
                
        draw_window(player,enermy)
        
        
if __name__ == "__main__":
    main()


