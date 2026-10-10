import math

print("Convert Radians to Degrees")
while True:
    d = input("Radians: ")
    try:
        d = float(d)
        r = d
        d = math.degrees(d)
        print(f"{r} radians is about {d % 360} degrees.")
        input()
        break
    except ValueError:
        print("Please input a number!")