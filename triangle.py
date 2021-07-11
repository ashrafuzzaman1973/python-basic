class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height = height
    def calculate_area(self):
        area =0.5*self.base*self.height
        print("Area =",area)

triangle1 = Triangle(10,20)
triangle1.calculate_area()

triangle2 = Triangle(25,30)
triangle2.calculate_area()