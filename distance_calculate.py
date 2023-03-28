import math

p1 = (23, -88)
p2 = (6, 42)

#your code goes here
#d=√((x2 - x1)² + (y2 - y1)²)
a = (p2[0]-p1[0])**2
b = (p2[1]-p1[1])**2
p = math.sqrt(a+b)
print(p)