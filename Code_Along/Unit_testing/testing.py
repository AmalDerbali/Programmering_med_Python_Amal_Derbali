from vector import Vector
import unittest

#v1 = Vector(1,1)
#print(v1)

class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2

    def create_2D_vector(self) -> "Vector":
        return Vector(self.x, self.y)

    # testing starts here - all tests must start with the word test_
    def test_create_2D_vector(self) -> None:
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))
    

    def test_create_5D_vector(self):
        v = Vector (1, 2, 3, 4, 5)
        self.assertEqual(v.numbers, (1, 2, 3, 4, 5))
    

    


if __name__ == "__main__":
    unittest.main()
    
  