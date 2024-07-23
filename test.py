import unittest
import my_python_area

class TestFigArea(unittest.TestCase):

    def test_circle_area(self):
        circle = my_python_area.Circle(10)
        self.assertEqual(circle.fig_area(), 314.1592653589793, 'Площадь круга неверна.')

    def test_triangle_area(self):
        triangle = my_python_area.Triangle(5,4,3)
        self.assertEqual(triangle.fig_area(), 6.0, 'Площадь треугольника неверна.')

    def test_triangle_perimeter(self):
        triangle = my_python_area.Triangle(5,4,3)
        self.assertEqual(triangle.fig_perimeter(), 12, 'Периметр треугольника неверен.')

    def test_triangle_is_not_right(self):
        triangle = my_python_area.Triangle(5,4,3)
        self.assertEqual(triangle.is_right(), 'Не Прямоугольный.', 'Это прямоугольный треугольник.') 

    
    def test_triangle_is_right(self):
        triangle = my_python_area.Triangle(6,8,10)
        self.assertEqual(triangle.is_right(), 'Прямоугольный.', 'Это не прямоугольный треугольник.')        



if __name__ == '__main__':
    unittest.main()        


