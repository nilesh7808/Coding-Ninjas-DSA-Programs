import math
class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "This Point is at ("+ str(self.__x) + "," + str(self.__y)+ ")"

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __lt__(self, other):
        return (self.__x**2 + self.__y**2) < (other.__x**2 + other.__y**2)

P1 = Point(1,2)
P2 = Point(3,4)
P3 = P1 + P2
print(P3)
print(P1<P2)
print(P1>P2)
