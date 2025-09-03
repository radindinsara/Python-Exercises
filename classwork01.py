def spruce(size):
    print("A spruce is coming!")

    for i in range(1, size + 1):
        tspaces = " " * (size - i)
        tstars = "*" * (2 * i - 1)
        print(tspaces + tstars)

    spaces_trunk = " " * (size - 1)
    print(spaces_trunk + "*")

spruce(6)