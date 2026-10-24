def square():
    A = int(input("Input A = "))
    B = int(input("Input B = "))
    C = int(input("Input C = "))

    KR = (1/4 * (A**2)) + (1/4 * (B**2) - C)

    if KR == 0:
        print("Lingkaran titik")
    elif KR > 0:
        print("Lingkaran nyata")
    else:
        print("Lingkaran khayal")

square()