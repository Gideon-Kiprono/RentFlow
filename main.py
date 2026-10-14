# from vehicle import Vehicle, EconomyCar,SUV,LuxuryCar


# # axio = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)
# # prado = SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000)
# # merc = LuxuryCar("KDL 789C", "Mercedes-Benz", "E-Class", 2024, 15000)

# # for car in [axio, prado, merc]:
# #     print(f"{car.make} {car.model}: KSh {car.calculate_rental_cost(3):,}")


# axio = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)

# print(axio.is_available())   # what do you expect here?

# axio.mark_as_rented()
# print(axio.is_available())   # and here?

# axio.mark_as_available()
# print(axio.is_available())   # and here?

# # 1. Polymorphism: expect 12,000 / 26,000 / 49,500
# prado = SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000)
# merc = LuxuryCar("KDL 789C", "Mercedes-Benz", "E-Class", 2024, 15000)

# for car in [axio, prado, merc]:
#     print(f"{car.make} {car.model}: KSh {car.calculate_rental_cost(3):,}")

# # 2. Negative rate: expect a clear error message, not a crash
# try:
#     EconomyCar("KDK 999Z", "Toyota", "Vitz", 2020, -500)
# except ValueError as error:
#     print(f"Error: {error}")

# # 3. Abstraction: expect a message, not a crash
# try:
#     Vehicle("KDK 123A", "Toyota", "Axio", 2022, 4000)
# except TypeError as error:
#     print(f"Error: {error}")


# axio.display_details()
# print()
# axio.mark_as_rented()
# axio.display_details()


# from customer import Customer

# # Checking valid customer
# john = Customer("C001", "John Kamau", "0712345678","12345678", "DL45821")
# john.display_details()

# # New customer has no history
# john.view_rental_history()

# # add_rental changes state
# john.add_rental("test rental")
# john.view_rental_history()

# # Missing licence is rejected
# for bad_licence in ["", "   "]:
#     try:
#         Customer("C002", "Jane Wanjiru", "0722222222", "87654321", bad_licence)
#     except ValueError as error:
#         print(f"Error: {error}")

# from vehicle import SUV
# from customer import Customer
# from rental import Rental

# john = Customer("C001", "John Kamau", "0712345678", "12345678", "DL45821")
# prado = SUV("KDJ 456B", "Toyota", "Prado", 2023, 8000)

# # 1. Create a rental: base cost should be 34,000 (4 days + service charge)
# rental = Rental("R001", john, prado, 4)
# print(rental.base_cost)                 # 34000
# print(rental.calculate_total())         # 34000

# # 2. Return 2 days late: late fee 3,200, total 37,200
# rental.complete_rental(actual_days=6)
# print(rental.late_fee)                  # 3200
# print(rental.calculate_total())         # 37200
# print(rental.status)                    # COMPLETED

# # 3. Rule 8: completing twice must fail
# try:
#     rental.complete_rental(actual_days=6)
# except ValueError as error:
#     print(f"Error: {error}")

# # 4. Payment status
# print(rental.is_paid())                 # False
# rental.mark_as_paid()
# print(rental.is_paid())                 # True

# # 5. Rule 10: paying twice must fail
# try:
#     rental.mark_as_paid()
# except ValueError as error:
#     print(f"Error: {error}")

# # 6. Rule 5: zero days must fail
# try:
#     Rental("R002", john, prado, 0)
# except ValueError as error:
#     print(f"Error: {error}")

# # 7. Paying before completion must fail
# fresh = Rental("R003", john, prado, 2)
# try:
#     fresh.mark_as_paid()
# except ValueError as error:
#     print(f"Error: {error}")

# # Test the early-return case.
# early = Rental("R004", john, prado, 4)
# early.complete_rental(actual_days=2)
# print(early.late_fee)    # expect 0, not negative

# rental.display_rental_details()

#  ===Testing the rental_system.py logic
from vehicle import EconomyCar,SUV
from customer import Customer
from rental_system import CarRentalSystem


system = CarRentalSystem("SafariDrive Rentals")
system.add_vehicle(EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000))
system.add_vehicle(SUV("KDJ 465B", "Toyota", "Prado", 2023, 8000))
system.register_customer(Customer("C001", "John Kamau", "0712345678", "12345678","DL45821"))


print(len(system.vehicles), len(system.customers))

print(system.find_vehicle("KDK 123A").model)   # Axio
print(system.find_vehicle("XXX"))              # None
print(system.find_customer("C001").name)        # John Kamau
print(system.find_customer("C999"))             # None

premio = EconomyCar("KAA 123A", "Toyota", "Premio", 2020, 4000)
lexus = SUV("KBB 456B", "Toyota", "Lexus", 2013, 8000)

system.add_vehicle(premio)
system.add_vehicle(lexus)

premio.mark_as_rented()
system.show_available_vehicles()



print(system.revenue)        # reading works: 0

try:
    system.revenue = 5000    # writing is blocked
except AttributeError as error:
    print(f"Error: {error}")

# system.__revenue = 10_000_000
# print(system.revenue)        # still 0

# duplicate check
try:
    system.add_vehicle(EconomyCar("KDK 123A", "Toyota", "Vitz", 2020, 3500))
except ValueError as error:
    print(f"Error: {error}")