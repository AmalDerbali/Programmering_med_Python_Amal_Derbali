from geometry_shapes_2D import Circle
import math



class Sphere (Circle):
    def __init__ (self, radius:float, x_value: float = 0, y_value: float = 0, z_value: float = 0) -> None:
        super().__init__(radius, x_value, y_value)
        self.z_value = z_value
    
    @property
    def z_value (self) -> float:
        return self._z_value
    
    @z_value.setter
    def z_value(self, z_value: float) -> None:
        if not isinstance(z_value, (int, float)):
            raise TypeError (f"z_value must be a int or float, not a {type(z_value)}.")
        if z_value <= 0:
            raise TypeError(f"z_value must be > 0.")
        self._z_value = z_value
        return self._z_value
    
    def surface_area_sphere (self):
        return ((self.radius**2)*math.pi*4)
    
    def volume_sphere (self):
        return (4/3*(self.radius**3)*math.pi)
    
    def point_inside_sphere (self, x, y, z):
        euclidean = (((self.x_value - x)**2 + (self.y_value - y)**2 + (self.z_value - z)**2)**0.5)
        if euclidean < self.radius:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False

        if self.radius == other.radius:
            return True
        else:
            return False
    
    def translate(self, new_x, new_y, new_z) -> None:
        if not isinstance (new_z, (int, float)):
            raise ValueError ("The value new_z must be int or float")
        if new_z == 0:
            raise ValueError("The value can't be 0")
        if new_z < 0:
            raise ValueError("The value can't be negative")
        self._x_value = new_x
        self._y_value = new_y
        self._z_value = new_z
         
    

    def __repr__(self): # gives informations about the size and position of the sphere.
        return f"The radius of the circle is: {self.radius}. The geometric center is: ({self.x_value}, {self.y_value}, {self.z_value})."
    

