
class Enemy():
    def __init__(self, image, x_coordinate, y_coordinate):
        self.is_alive = True
        self.img = image
        self.xcor = x_coordinate
        self.ycor = y_coordinate
        self.direction = 1
        self.width = image.get_width()
        self.height = image.get_height()
    
    def show(self, game_display):
        game_display.blit(self.img, (self.xcor, self.ycor))
    
    def has_collided_with_right_wall(self, right_wall_x_location):
        return self.xcor + self.width >= right_wall_x_location
    
    def has_collided_with_left_wall(self, left_wall_x_location):
        return self.xcor <= left_wall_x_location
    
    def move_over(self, amount_to_move):
        self.xcor += amount_to_move

    def move_down(self, amount_to_move):
        self.ycor += amount_to_move
    