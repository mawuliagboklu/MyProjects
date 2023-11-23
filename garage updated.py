import random
import string

N = 5
code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def Igarage_ticketing_system():
    print("Welcome to Igarage.. Your vehicle, our priority")
    car_number = input("Car number: ")
    car_color = input("Car color: ")
    car_brand = input("Car brand: ")
    number_of_cars = int(input("How many cars have you brought?"))

    services = []
    while True:
        print("Choose from any of our available services:")
        print("a. Car body maintenance")
        print("b. Air condition maintenance")
        print("c. Car engine maintenance")
        print("q. Quit")
        service_choice = input("Enter your choice: ")

        if service_choice == 'q':
            break

        if service_choice in ['a', 'b', 'c']:
            service_sub_choice = input("Choose a sub-service: ")
            services.append((service_choice, service_sub_choice))

    print("Your garage code is:", code)
    print("Number of cars:", number_of_cars)
    print("Services requested:")
    for service in services:
        print(f"Service {service[0]} - Sub-service {service[1]}")

Igarage_ticketing_system()
