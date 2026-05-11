class Circle:
    """
    A class representing a circle with class-level tracking of all instances.
    
    Class Attributes:
        pi (float): The mathematical constant pi (3.1415)
        all_circles (list): A collection of all Circle instances created
    
    Attributes:
        radius (float): The radius of the circle.
    """
    
    pi = 3.1415
    all_circles = []
    
    def __init__(self, radius=None) -> None:
        """
        Initialize a new Circle object.
        """
        if radius is None:
            self.radius = 1
        else:
            self.radius = radius
        
        Circle.all_circles.append(self)
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle 
        """
        return Circle.pi * self.radius ** 2
    
    @staticmethod
    def total_area() -> float:
        """
        Calculate the total area of all circle instances.
        
        Returns:
            float: The sum of areas of all circles created
        """
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total
    
    def __str__(self) -> str:
        """
        Return string representation of the circle's radius.
        
        Returns:
            str: The radius as a string
        """
        return str(self.radius)
    

def main() -> None:
    """
    The main function demonstrating the Circle class functionality.
    """

    c1 = Circle()
    c2 = Circle(7)
    c3 = Circle(5)
    
    print(c2.area())
    print(c3)
    print(Circle.pi)
    print(Circle.all_circles)
    print(Circle.total_area())
    
    print(len(c3.__class__.all_circles))


if __name__ == "__main__":
    main()
