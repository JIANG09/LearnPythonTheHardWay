def add(a, b):
    print("ADDING %d + %f" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just function!")

age = add(100, 5)
height = subtract(7008, 4)
weight = multiply(1000, 2)
iq = divide(1001, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %f" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

step_1 = divide(iq, 3)
step_2 = multiply(weight, step_1)
step_3 = subtract(height, step_2)
what = add(age, step_3)

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")


