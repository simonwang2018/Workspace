#建立一个程序计算不同形状的面积，三角形和正方形。
class Triangle: #计算三角形面积
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        area = self.width * self.height / 2.0
        return area
myTriangle = Triangle(4,5)
print (myTriangle)
class Square: #计算正方形面积
    def __init__(self,size):
        self.size = size
    def getArea(self):
        area = self.size * self.size
        return area
mySquare = Square(7)
print (mySquare)