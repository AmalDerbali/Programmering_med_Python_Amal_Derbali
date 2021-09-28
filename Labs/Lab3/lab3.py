import math

class GeometricClass:
    def __init__(self, x_value : float = 0, y_value:float = 0) -> None:
        self.x_value = x_value
        self.y_value = y_value
    
    @property
    def x_value (self) -> float:
        return self._x_value

    @property
    def y_value (self) -> float:
        return self._y_value
    
    @x_value.setter
    def x_value(self, x_value: float) -> None:
        if not isinstance(x_value, (float)):
            raise TypeError (f"The value x must be a float, not a {type(x_value)}.")
        if x_value <= 0:
            raise TypeError(f"The value x must be > 0.")
        self._x_value = x_value
        return self._x_value

    @y_value.setter
    def y_value(self, y_value: float) -> None:
        if not isinstance(y_value, (float)):
            raise TypeError (f"The value y must be a float, not a {type(y_value)}.")
        if y_value <= 0:
            raise TypeError(f"The value y must be > 0.")
        self._y_value = y_value
        return self._y_value


class Circle (GeometricClass):
    def __init__ (self, x_value, y_value, radius:float) -> None:
        super().__init__(x_value, y_value)
        self.radius = radius

    @property
    def radius (self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, radius: float) -> None:
        if not isinstance(radius, (float)):
            raise TypeError (f"The radius must be a float, not a {type(radius)}.")
        if radius <= 0:
            raise TypeError(f"The radius must be > 0.")
        self._radius = radius
        return self._radius
    
    def area_circle (self):
        return ((self.radius**2)*math.pi)
    
    def circumference_circle (self):
        return (2*self.radius*math.pi)

    # checking if a point is inside the circle based on : 
    # https://math.stackexchange.com/questions/198764/how-to-know-if-a-point-is-inside-a-circle

    def inside_circle (self, x, y):
        euclidean = (((self.x_value - x)**2 + (self.y_value - y)**2)**0.5)
        if euclidean < self.radius:
            return True
        else:
            return False









class Rectangle (GeometricClass):
    def __init__ (self, x_value, y_value, side1: float, side2: float) -> None:
        super().__init__(x_value, y_value)
        self.side1 = side1
        self.side2 = side2

    @property
    def side1 (self) -> float:
        return self._side1
    
    @side1.setter
    def side1(self, side1: float) -> None:
        if not isinstance(side1, (float)):
            raise TypeError (f"The side must be a float, not a {type(side1)}.")
        if side1 <= 0:
            raise TypeError(f"The side must be > 0.")
        self._side1 = side1
        return self._side1 

    @property
    def side2 (self) -> float:
        return self._side2
    
    @side2.setter
    def side2(self, side2: float) -> None:
        if not isinstance(side2, (float)):
            raise TypeError (f"The side must be a float, not a {type(side2)}.")
        if side2 <= 0:
            raise TypeError(f"The side must be > 0.")
        self._side2 = side2
        return self._side2

    def area_rectangle(self):
        return self.side1*self.side2
    
    def circumference_rectangle(self):
        return ((self.side1*2)+(self.side2*2))   