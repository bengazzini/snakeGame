class Bullet():
    def __init__(self, image, x_coordinate, y_coordinate):
        self.is_alive = True
        self.img = image
        self.xcor = x_coordinate
        self.ycor = y_coordinate
        self.width = image.get_width()
        self.height = image.get_height()
    def show(self, game_display):
        game_display.blit(self.img, (self.xcor, self.ycor))
    def move(self):
        self.ycor -= 10
    def has_collided_with_top_wall(self, top_wall_y_location):
        return self.ycor <= top_wall_y_location