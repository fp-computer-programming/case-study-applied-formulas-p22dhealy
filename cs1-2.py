#author: DMH 10/12/21

P = int(input("What is the principal investment?"))

r = float(input("What is the annual interest rate?"))

t = int(input("What is the amount of time the money is invested?"))

A = P * ((1 + (r / 12)) ** (12 * t))

print(A)