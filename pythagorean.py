import math

print("Pythagorean Theorem Calculator")
while True:
    a = input("a: ")
    try:
        a = float(a)
        break
    except ValueError:
        print("Please input a number!")

while True:
    b = input("b: ")
    try:
        b = float(b)
        break
    except ValueError:
        print("Please input a number!")

a, b = a ** 2, b ** 2
c = math.sqrt(a + b)

print(f"c = {c}")