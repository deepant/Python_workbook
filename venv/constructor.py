class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    def move(self):
        print('move')
    def termianl(self):
        print('draw')


point1 = Point(10,20)
print(point1.x)
point1.termianl()
point1.move()
