from bullet import Bullet

class Hero():
    def __init__(self, image, x_coordinate, y_coordinate):
        self.is_alive = True
        self.img = image
        self.xcor = x_coordinate
        self.ycor = y_coordinate
        self.direction = 0
        self.speed = 10
        self.width = image.get_width()
        self.bullets_fired = []
    def show(self, game_display):
        game_display.blit(self.img, (self.xcor, self.ycor))
    def has_collided_with_right_wall(self, right_wall_x_location):
        return self.xcor + self.width >= right_wall_x_location
    def has_collided_with_left_wall(self, left_wall_x_location):
        return self.xcor <= left_wall_x_location
    def shoot(self, bullet_image):
        new_bullet = Bullet(bullet_image, self.xcor + self.width / 2 - bullet_image.get_width() / 2, self.ycor)
        self.bullets_fired.append(new_bullet)
    def remove_dead_bullets(self):
        for i in range(len(self.bullets_fired) -1, -1, -1):
            if self.bullets_fired[i].is_alive == False:
                self.bullets_fired.pop(i)
        
    def move(self, left_wall, right_wall):
        if self.direction == -1 and self.has_collided_with_left_wall(left_wall) == False:
            self.xcor += self.speed * self.direction
        elif self.direction == 1 and self.has_collided_with_right_wall(right_wall) == False:
            self.xcor += self.speed * self.direction

    def set_direction_right(self):
        self.direction = 1
    def set_direction_left(self):
        self.direction = -1
    def set_direction_none(self):
        self.directon = 0



