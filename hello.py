import sys

x = 1

print("Hello ")
x = 5
y = 10
print(x)
print(y)
y += x
if y > 2:
    print("bad")
print(y)

test = "teste"
print("Hello")
print("teste")


def greet(who_to_meet):

    greeting = "Hello, {}".format(who_to_meet)
    return greeting
