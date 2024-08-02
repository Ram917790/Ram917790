pi=3.14
total=0
def add(*args):
    for arg in args:
        total+=arg


def square(x):
    return x**2

def cube(x):
    return x**3

def circumference(radius):
   return 2 * pi * radius

def area(radius):
   return pi * radius ** 2

print(add(2,6))