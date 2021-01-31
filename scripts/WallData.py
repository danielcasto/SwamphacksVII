class WallData(): 
# Note: Length is the vertical size of the wall, Width is the horizontal size of the wall.
# Length and width are in pixels!
# Also, x_pos and y_pos are for the TOP LEFT CORNER of the wall!
    def __init__(self, length, width, x_pos, y_pos):
        self.length = length
        self.width = width
        self.x_pos = x_pos
        self.y_pos = y_pos
