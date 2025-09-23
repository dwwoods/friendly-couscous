class Point:
    def move(self): # you can define methods in the class
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.x = 10 # they can also have attributes
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 30
point2.y = 40
print(point2.x)