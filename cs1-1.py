#author: DMH 10/12/21

x1 = int(input("What is the x coordinate of the first point?"))

y1 = int(input("what is the y coordinate of the first point?"))

x2 = int(input("What is the x coordinate of the second point?"))

y2 = int(input("What is the y coordinate of the second point?"))

distance = .5 ** (((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print("The disctance between the two points is " + str(distance))