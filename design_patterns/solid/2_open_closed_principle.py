from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    small = 1
    medium = 2
    large = 3

class Product:
    """
     Class Product to show open close principle.
     Software entities (classes, modules, functions, etc.) should be open for extension, 
     but closed for modification.

     A class will be said to be open if it is still available for extension. 
     For example, it should be possible to add fields to the data structures it contains, 
     or new elements to the set of functions it performs.
     
     A class will be said to be closed if [it] is available for use by other classes. 
     This assumes that the class has been given a well-defined, stable description 
     (the interface in the sense of information hiding).
    """    
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

# Wrong approach of class modification
class ProductFilter:
    def filter_by_color(self, products, color):
        pass
    
