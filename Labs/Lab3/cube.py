from lab3 import Rectangle

class Cube(Rectangle):
    def __init__(self, edge = float, x_value: float = 0, y_value: float = 0, z_value: float = 0) -> None:
        super().__init__(x_value, y_value, z_value)
        self.edge = edge

    @property
    def edge (self) -> float:
        return self._edge
    
    @edge.setter
    def edge(self, edge: float) -> None:
        if not isinstance(edge, (int, float)):
            raise TypeError (f"The edge must be a int or float, not a {type(edge)}.")
        if edge <= 0:
            raise TypeError(f"The edge must be > 0.")
        self._edge = edge
        return self._edge
    
    def surface_area_cube (self):
        return ((self.edge**2)*6)
    
    def volume_cube (self):
        return (self.edge**3)
    
    def point_inside_cube (self, x = float, y = float, z = float) -> bool:
        if ((self.x_value - self.edge/2) <= x <= (self.x_value + self.edge/2) 
            and (self.y_value - self.edge/2) <= y <= (self.y_value + self.edge/2) 
            and (self.z_value - self.edge/2) <= z <= (self.z_value + self.edge/2)):
            return True
        else:
            return False
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False

        if self.edge == other.edge:
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
         
    def __repr__(self):
        return f"The cube has an edge of {self.edge}. The geometric center is: ({self.x_value}, {self.y_value}, {self.z_value})."
   

    