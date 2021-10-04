from geometry_shapes_2D import GeometricClass
from geometry_shapes_2D import Circle
from geometry_shapes_2D import Rectangle
from sphere import Sphere 
from cube import Cube
import unittest

class TestGeometricClass(unittest.TestCase):
        
    def setUp(self) -> None:
    # Initialises values to use for x-value and y-value.
        self.x_value, self.y_value = 3, 3
    
    def create_geometricClass(self) -> "GeometricClass": 
        #Returns a GeometricCalss object, using the values from the setUp function.
        return GeometricClass(self.x_value, self.y_value)
    
    def test_create_GeometricClass(self) -> None:
        geo = self.create_geometricClass()
        self.assertEqual(geo.x_value, self.x_value), (geo.y_value,self.y_value)
        
        geo = GeometricClass()
        self.assertEqual(geo.x_value, geo.y_value), (3, "two")
        
    
    
class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
    # Initialises values to use for radius, x-value and y-value.
        self.radius, self.x_value, self.y_value = 3, 3, 0
    
    def create_circle(self) -> "Circle": 
        #Returns a Circle object, using the values from the setUp function.
        return Circle(self.radius, self.x_value, self.y_value)

    def test_create_circle(self) -> None:
        circ = self.create_circle()
        self.assertEqual(circ.radius, self.radius), (circ.x_value, self.x_value), (circ.y_value,self.y_value)
        
        circ = Circle(2)
        self.assertEqual(circ.x_value, circ.y_value), (2, "two", -3)     
        
    def test_translate(self):
        #tests if a TypeError is raised when entering a str in the parameter.
        circ = self.create_circle()        
        with self.assertRaises(TypeError):
            circ.translate("4", 2)
        with self.assertRaises(TypeError):
            circ.translate(4, "2")

    def test_translate(self):
        circ = self.create_circle()        
        circ.translate(3, 2)
        self.assertEqual((circ.x_value, circ.y_value), (3, 2))

    def test_area_circle(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its area is 19.63.
        circ1 = Circle(2.5)
        self.assertAlmostEqual(circ1.area_circle(), 19.63, places = 2)

    def test_circumference_circle(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its circumference is 15.71.
        c1 = Circle(2.5)
        self.assertAlmostEqual(c1.circumference_circle(), 15.71, places = 2)   

    def test_point_inside_circle(self):
        circ = self.create_circle()
        self.assertEqual(circ.point_inside_circle(2, -2), True)
        self.assertEqual(circ.point_inside_circle(1.3, -6), False) 

    def test_equality(self):
        circ2 = Circle(3, 2, 5)
        circ3 = Circle(5, 2, 2)
        self.assertEqual(circ2 == circ3, False) 

        circ = Circle(4, 2, 3)
        rect = Rectangle(4, 2, 2, 1)
        self.assertEqual(circ == rect, False)


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.side1, self.side2, self.x_value, self.y_value = 3, 2, 0, 1
    
    def create_rectangle(self) -> "Rectangle": 
        return Rectangle(self.side1, self.side2, self.x_value, self.y_value)

    def test_create_rectangle(self) -> None:
        rect1 = self.create_rectangle()
        self.assertEqual(rect1.side1, self.side1), (rect1.side2, self.side2), (rect1.x_value, self.x_value), (rect1.y_value, self.y_value)
        
        rect1 = Rectangle(3, 2)
        self.assertEqual(rect1.x_value, rect1.y_value), (3, "two")  
    
    def test_translate(self):
        rect3 = self.create_rectangle()        
        rect3.translate(3, 2)
        self.assertEqual((rect3.x_value, rect3.y_value), (3, 2))
    
    
    def test_area_rectangle(self):
        rect = self.create_rectangle()
        self.assertEqual(rect.area_rectangle(), 6)
    
    def test_circumference(self):
        rect = self.create_rectangle()
        self.assertEqual(rect.circumference_rectangle(), 10)

    def test_point_inside_rectangle(self):
        rect = self.create_rectangle()
        self.assertEqual(rect.point_inside_rectangle(2, 1), False)
        self.assertEqual(rect.point_inside_rectangle(1.3, 6), False) 

    def test_equality(self):
        rec = Rectangle(4, 3, 2, 5)
        rec1 = Rectangle(7, 5, 2, 2)
        self.assertEqual(rec == rec1, False) 
    

class TestSphere(unittest.TestCase):

    def setUp(self) -> None:
        self.radius, self.x_value, self.y_value, self.z_value = 2, 3, 3, 3 
    
    def create_sphere(self) -> "Sphere": 
        return (self.radius, self.x_value, self.y_value, self.z_value)
    
    def test_create_sphere(self) -> None:
        sph = self.create_sphere()
        self.assertEqual(sph.radius, self.radius), (sph.x_value, self.x_value), (sph.y_value, self.y_value), (sph.z_value, self.z_value)
        
        sph = Sphere()
        self.assertEqual(sph.radius, sph.x_value, sph.y_value, sph.z_value), (2, 3, 4)

 
    

if __name__ == "__main__":
    unittest.main() 

