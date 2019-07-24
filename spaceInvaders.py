import pygame

#MEDIA FILES
player_image = pygame.image.load('spaceship.gif')

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((400, 600))
score_font = pygame.font.SysFont('Times New Roman', int(22 * 0.065), True)
title_font = pygame.font.SysFont('Times New Roman', int(26 * 0.2), True)
pygame.display.set_caption('SPACE INVADERS!')

x_coordinate = 50
y_coordinate = 100

def handle_events():
    global x_coordinate, y_coordinate, is_playing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_coordinate -= x_coordinate - 10
            elif event.key == pygame.K_RIGHT:
                x_coordinate += x_coordinate + 10



#in the main game loop
is_playing = True
while is_playing:
     handle_events()
     game_display.blit(game_display, (0, 0))
     game_display.fill((0, 0, 0))
     game_display.blit(player_image, (x_coordinate, y_coordinate))
     # score_text = score_font.render(str(snake.score), False, (255, 255, 255))
     #game_display.blit(score_text, (0,0))
     pygame.display.update()
     clock.tick(30)

pygame.display.quit()
pygame.quit()



