import math

print("Pythagorean Theorem Calculator")
a = input("a: ")
b = input("b: ")

a, b = float(a), float(b)

a, b = a ** 2, b ** 2
c = math.sqrt(a + b)

print(c)