options = {1, 2, 3, 4, 5}

print("Calculators:\n")
print("""
      1: Degrees to Radians\n
      2: Radians to Degrees\n
      3: Quadratic Roots\n
      4: Pythagorean Theorem\n
      5: Number Game\n
      """)

while True:
    x = input("Select an option(1–5):\n")
    x = int(x)
    if x in options:
        if x == 1:
            import radians
        elif x == 2:
            import degrees
        elif x == 3:
            import quadratics
        elif x == 4:
            import pythagorean
        elif x == 5:
            import numbergame
        break
    else:
        print("Please enter a valid input (1–5).")