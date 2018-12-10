cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  # subtraction
cars_driven = drivers  # give cars_driven a same value as drivers
carpool_capacity = cars_driven * space_in_a_car  # multiplication
average_passenger_per_car = passengers / cars_driven  # division

print("There are", cars, "cars available.")  # variable cars will print out since it has been given a value of 100.
print("There are only", drivers, "drivers available.")
# variable driver will be print out since it has been given a value of 30.
print("There are", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")  # the calculation will be done when print out.
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")
# the calculation will be done when printing out.


# Practice
i = 190
x = 2
j = i ^ x

print(j % i)
