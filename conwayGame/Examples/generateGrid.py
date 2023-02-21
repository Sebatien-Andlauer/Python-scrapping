def grid_print(area, units):
    for _ in range(area):
        print(("+" + "-" * units) * area + "+")
        for _ in range(units):
            print(("|" + " " * units) * area + "|")
    print(("+" + "-" * units) * area + "+")

grid_print(4, 4)