import math

print("Convert Degrees to Radians")
while True:
    d = input("Degrees: ")
    try:
        r = math.radians(float(d))
        print(f"{d} degrees is about {r % (2 * math.pi)} or {(r % (2 * math.pi))/math.pi}π radians.")
        input()
        break
    except ValueError:
        print("Please input a number!")