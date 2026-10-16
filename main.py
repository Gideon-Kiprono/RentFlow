print("RUNNING NEW VERSION")

from vehicle import EconomyCar, SUV, LuxuryCar
from customer import Customer
from rental_system import CarRentalSystem

system = CarRentalSystem("SafariDrive Rentals")

print("\n--- Setting up the fleet ---")
fleet = [
    EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000),
    SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000),
    LuxuryCar("KBM 678S", "Mercedes-Benz", "E-Class", 2021, 15000),
    EconomyCar("KDV 809Z", "Toyota", "Demio", 2016, 4000),
    SUV("KCJ 456L", "Toyota", "Lexus", 2021, 8000),
    LuxuryCar("KDM 123B", "Audi", "e-tron", 2026, 15000),
]
for vehicle in fleet:
    system.add_vehicle(vehicle)

print("\n--- Registering customers ---")
customers = [
    Customer("C001", "John Kamau", "0712345678", "12345678", "DL45821"),
    Customer("C002", "Mary Wanjiku", "0723456789", "23456789", "DL56932"),
    Customer("C003", "Gideon Kiprono", "0789678904", "45678904", "DL67893"),
]
for customer in customers:
    system.register_customer(customer)


system.show_available_vehicles()
system.search_vehicles(vehicle_type="SUV")