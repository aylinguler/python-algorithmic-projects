# Polygon Area Project
# A Python implementation of a geometry tool that calculates properties of 
# Rectangles and Squares.

class Rectangle:
    """
    Represents a rectangle shape with basic geometric calculations 
    and a visual string representation.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        #Calculates the area: width * height.
        return self.width * self.height
    
    def get_perimeter(self):
        #Calculates the perimeter: 2 * width + 2 * height.
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        #Calculates the diagonal using the Pythagorean theorem.
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        #Returns a string representation using asterisks.
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        
        line = "*" * self.width + "\n"
        return line * self.height

    def get_amount_inside(self, shape):
        #Calculates how many instances of 'shape' fit inside this rectangle.
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """
    Square subclass of Rectangle. Maintains equal width and height.
    """
    def __init__(self, side):
        # Initializes the parent class with side as both width and height
        super().__init__(side, side)
    
    def set_side(self, side):
        #Sets both width and height to maintain square proportions.
        self.width = side
        self.height = side
    
    def set_width(self, width):
        #Overrides Rectangle set_width to update height simultaneously.
        self.set_side(width)
    
    def set_height(self, height):
        #Overrides Rectangle set_height to update width simultaneously.
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


if __name__ == "__main__":
    # --- Integration Testing ---
    # Create a rectangle and test basic functionality
    rect = Rectangle(10, 5)
    print(rect)
    print(f"Area: {rect.get_area()}")
    print(f"Picture:\n{rect.get_picture()}")
    
    # Create a square and verify inheritance
    sq = Square(9)
    print(sq)
    print(f"Square Area: {sq.get_area()}")
    
    # Test method overriding
    sq.set_width(4)
    print(f"Square after set_width(4): {sq}")
    
    # Test shape containment
    rect.set_width(16)
    rect.set_height(8)
    print(f"Number of squares that fit in rectangle: {rect.get_amount_inside(sq)}")