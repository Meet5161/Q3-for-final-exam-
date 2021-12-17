class AnalyzeTriangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validateTringle(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

print (" Enter the angles of tringle")
a = int (input ('Value of a= '))
b = int (input ('Value of b= '))
c = int (input ('Value of c= '))

if a + b>= c and b + c >= a and c + a >=b:
    print (" It is triangle.")
else:
    print(" this is not valid entry")


if a==b==c:
    print ('\n It is Equilateral triangle')

elif a==b or b==c or c==a:
    print ('\n It is Isosceles triangle')

else:
    print (" \n Scalene triangle ")

import datetime

now = datetime.datetime.now()

print("\n Today’s date: , today's time:")
print(now.strftime("%m-%d-%Y") , now.strftime("%H-%M-%S"))