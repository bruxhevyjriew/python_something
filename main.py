options = {1, 2, 3, 4, 5, 6}
while True:
    print("Calculators:\n")
    print("""
      1: Degrees to Radians\n
      2: Radians to Degrees\n
      3: Quadratic Roots\n
      4: Pythagorean Theorem\n
      5: Number Game\n
      6: Exit\n
      """)

    x = input("To select an option, enter the corresponding number (1–6):\n")
    try:
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
            elif x == 6:
                break
        else:
            print("Please enter a valid input.")
    except ValueError:
        print("Please enter a valid input.")