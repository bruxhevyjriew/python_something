import math

print("Quadratic Formula Calculator")
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
while True:
    c = input("c: ")
    try:
        c = float(c)
        break
    except ValueError:
        print("Please input a number!")

try:
    x1 = (-b + math.sqrt((b ** 2) - (4 * a * c)))/(2 * a)
    x2 = (-b - math.sqrt((b ** 2) - (4 * a * c)))/(2 * a)
    if x1 == x2:
        print(f"This quadratic has one root at ({x1}, 0.0)")
    else:
        print(f"This quadratic has roots at ({x1}, 0.0) and ({x2}, 0.0)")
except ValueError:
    print("This quadratic has no real roots.")
except ZeroDivisionError:
    print("Error: Division by zero")