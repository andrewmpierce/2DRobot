class Robot():

    def __init__(self):
        self.position = [0,0]
        self.orientation = 0

    def move(self):
        if self.orientation == 0:
            self.position[1] += 1
        if self.orientation == 90:
            self.position[0] += 1
        if self.orientation == 180:
            self.position[1] -= 1
        if self.orientation == 270:
            self.position[0] -= 1

    def turn_left(self):
        if self.orientation == 0:
            self.orientation = 270
        else:
            self.orientation -= 90

    def turn_right(self):
        if self.orientation == 270:
            self.orientation = 0
        else:
            self.orientation += 90
