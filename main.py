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

print("\n--- Renting vehicles ---")
rental1 = system.rent_vehicle(customers[0], fleet[1], 4)   # John: Prado, 4 days
rental2 = system.rent_vehicle(customers[1], fleet[0], 3)   # Mary: Axio, 3 days
rental3 = system.rent_vehicle(customers[2], fleet[2], 2)   # Gideon: E-Class, 2 days
rental4 = system.rent_vehicle(customers[1], fleet[4], 5)   # Mary: Lexus, stays ACTIVE

rental1.display_rental_details()

print("\n--- Rule check: car already rented ---")
try:
    system.rent_vehicle(customers[2], fleet[1], 2)
except ValueError as error:
    print(f"Error: {error}")

system.show_active_rentals()

print("\n--- Returning vehicles ---")
system.return_vehicle(rental1, actual_days=6)                      # 2 days late
system.return_vehicle(rental2, actual_days=3)                      # on time
system.return_vehicle(rental3, actual_days=2, damage_charge=5000)  # damaged
rental1.display_rental_details()
system.show_completed_rentals()

print("\n--- Payments ---")
from payment import MpesaPayment, CardPayment, CashPayment
system.process_payment(MpesaPayment(rental1, "0712345678"))
system.process_payment(CashPayment(rental2, 15000))
system.process_payment(CardPayment(rental3, "4417"))

print("\n--- Rule check: paying twice ---")
try:
    system.process_payment(CashPayment(rental1, 40000))
except ValueError as error:
    print(f"Error: {error}")

print("\n--- Management report ---")
system.generate_report()