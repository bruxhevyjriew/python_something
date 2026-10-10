options = {1, 2, 3, 4}

print("Calculators:")
print("""
      1: Degrees to Radians\n
      2: Radians to Degrees\n
      3: Quadratic Roots\n
      4: Pythagorean Theorem
      """)

while True:
    x = input("Select an option(1–4):")
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
        break
    else:
        print("Please enter a valid input (1–4).")