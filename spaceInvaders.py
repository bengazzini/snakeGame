import pygame
from hero_class import Hero
from enemy import Enemy 

# GAME SETTINGS
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3

GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#MEDIA FILES
player_image = pygame.image.load('spaceship.gif')
bullet_image = pygame.image.load('bullet.gif')
enemy_image = pygame.image.load('enemy.gif')

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score_font = pygame.font.SysFont('Times New Roman', int(22 * 0.065), True)
title_font = pygame.font.SysFont('Times New Roman', int(26 * 0.2), True)
pygame.display.set_caption('SPACE INVADERS!')



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hero.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_right()
            elif event.key == pygame.K_SPACE:
                hero.shoot(bullet_image)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero.set_direction_none()
            elif event.key == pygame.K_RIGHT:
                hero.set_direction_none() 


hero = Hero(player_image, 200, GAME_BOTTOM_WALL - player_image.get_height())
enemies = []
enemies.append(Enemy(enemy_image, 25, 25))
enemies.append(Enemy(enemy_image, 50, 25))
enemies.append(Enemy(enemy_image, 75, 25))
enemies.append(Enemy(enemy_image, 100, 25))
enemies.append(Enemy(enemy_image, 125, 25))

#enemy = Enemy(enemy_image, 25, 25)

#in the main game loop
is_playing = True
while hero.is_alive:
    
    handle_events()

    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)


    #move each enemy down and change its direction if it hits a wall
    for enemy in enemies:
        if enemy.has_collided_with_left_wall(GAME_LEFT_WALL):
            for e in enemies:
                e.ycor += 10
                e.direction = 1
            break

        if enemy.has_collided_with_right_wall(GAME_RIGHT_WALL):
            for e in enemies:
                e.ycor += 10
                e.direction = -1
            break

    #Move each enemy over based on its direction
    for i in range(0, len(enemies)):
        enemies[i].xcor += 10 * enemies[i].direction
        
    for enemy in enemies:
        enemy.xcor += 4 * enemy.direction
   
    game_display.blit(game_display, (0, 0))
        
    game_display.fill((BLACK))

    pygame.draw.rect(game_display, WHITE, (GAME_SIDE_MARGIN, GAME_TOP_MARGIN, WINDOW_WIDTH - GAME_SIDE_MARGIN * 2, WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))
    pygame.draw.rect(game_display, BLACK,(GAME_LEFT_WALL, GAME_TOP_WALL, WINDOW_WIDTH - GAME_LEFT_WALL - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH, WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))

    hero.show(game_display)
    
    for i in range(0, len(enemies)):
        enemies[i].show(game_display)

    for bullet in hero.bullets_fired:
        if bullet.has_collided_with_top_wall(GAME_TOP_WALL):
            bullet.is_alive = False

    hero.remove_dead_bullets()
    for bullet in hero.bullets_fired:
        bullet.move()
        bullet.show(game_display)

     # score_text = score_font.render(str(snake.score), False, (255, 255, 255))
     #game_display.blit(score_text, (0,0))
    pygame.display.update()
    clock.tick(30)

pygame.display.quit()
pygame.quit()



