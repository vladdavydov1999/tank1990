import pygame 
from tank import Tank

# Initialization pyame
pygame.init()
clock = pygame.time.Clock()

# Create window game
screen = pygame.display.set_mode((960, 840)) # tuple on size window
pygame.display.set_caption("Tank3000")
battle_arena = pygame.Surface((780, 780)) #battlefield

# creating instences of classes
my_tank = Tank(battle_arena)

 
running = True
while running:
    

    #1 event handling
    for event in pygame.event.get(): #all event
        if event.type == pygame.QUIT:
            running = False 
            
    keys = pygame.key.get_pressed()
    my_tank.move(keys)
   
    #2 update game
    #3 update display
    # 1 step render background
    battle_arena.fill((0, 0, 0))
    screen.fill((90, 90, 90))

    # 2 step render object
    my_tank.blitme()
    screen.blit(battle_arena, (30, 30))
    # 3 step render display
    pygame.display.flip()
    clock.tick(30) #fps



pygame.quit() # deinitialization modul pygame
