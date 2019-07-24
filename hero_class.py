class Hero():
    def __init__(self, image, x_coordinate, y_coordinate):
        self.is_alive = True
        self.img = image
        self.xcor = x_coordinate
        self.ycor = y_coordinate
    def show(self, game_display):
        game_display.blit(self.img, (self.xcor, self.ycor))
    def has_collided_with_wall(self, left_wall_x_location, right_wall_x_location):
        if self.xcor < left_wall_x_location or self.xcor + self.img.get_width() > right_wall_x_location:
            return True
        return False