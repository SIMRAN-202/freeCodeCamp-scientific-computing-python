class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height
    
    def get_area(self):
        area = self.height * self.width
        return area
    
    def get_perimeter(self):
        perimeter = 2*(self.height + self.width)
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.height**2 + self.width**2)**0.5
        return diagonal
    
    def get_picture(self):
        picture_str = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            picture_str += "*" * self.width+"\n"
        return picture_str
    
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        return self.side

    def set_width(self, width):
        self.width = width
        self.height = width
        return self.width

    def set_height(self, height):
        self.width = height
        self.height = height
        return self.height

    def __str__(self):
        return f"Square(side={self.width})"



