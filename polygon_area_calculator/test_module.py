import unittest
from main import Rectangle, Square

class TestPolygonAreaCalculator(unittest.TestCase):

    def test_rectangle_initialization(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)

    def test_rectangle_setters(self):
        rect = Rectangle(4, 5)
        rect.set_width(10)
        rect.set_height(20)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)

    def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.get_area(), 20)

    def test_rectangle_perimeter(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.get_perimeter(), 18)

    def test_rectangle_diagonal(self):
        rect = Rectangle(3, 4)
        self.assertAlmostEqual(rect.get_diagonal(), 5.0)

    def test_rectangle_picture(self):
        rect = Rectangle(3, 2)
        self.assertEqual(rect.get_picture(), "***\n***\n")
        
        large_rect = Rectangle(60, 2)
        self.assertEqual(large_rect.get_picture(), "Too big for picture.")

    def test_rectangle_amount_inside(self):
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(2, 2)
        self.assertEqual(rect1.get_amount_inside(rect2), 10)

    def test_square_initialization(self):
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_square_setters(self):
        square = Square(5)
        square.set_side(8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

        square.set_width(4)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)

        square.set_height(6)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_square_area(self):
        square = Square(4)
        self.assertEqual(square.get_area(), 16)

    def test_square_perimeter(self):
        square = Square(4)
        self.assertEqual(square.get_perimeter(), 16)

    def test_square_picture(self):
        square = Square(2)
        self.assertEqual(square.get_picture(), "**\n**\n")

        large_square = Square(51)
        self.assertEqual(large_square.get_picture(), "Too big for picture.")

    def test_square_amount_inside(self):
        square1 = Square(10)
        square2 = Square(3)
        self.assertEqual(square1.get_amount_inside(square2), 9)

if __name__ == "__main__":
    unittest.main()
