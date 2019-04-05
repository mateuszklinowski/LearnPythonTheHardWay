cars = 100
spece_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpoll_capacity = cars_driven * spece_in_a_car
avarage_passenger_per_car =  passengers / cars_driven

print("There are ", cars, " cars available")
print("We have", passengers, "to carpoll today")
