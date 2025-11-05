lebar = 10
tinggi = 5

for y in range (tinggi):
    for x in range (lebar):
        if x == 3 and y == 2:
            print("x", end=" ")
        else:
                print(".", end= " ")
    print ()