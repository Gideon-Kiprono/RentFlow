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

# #  ===Testing the rental_system.py logic
from vehicle import EconomyCar,SUV
from customer import Customer
from rental_system import CarRentalSystem

axio = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)
prado = SUV("KDJ 465B", "Toyota", "Prado", 2023, 8000)
john = Customer("C001", "John Kamau", "0712345678", "12345678", "DL45821")


system = CarRentalSystem("SafariDrive Rentals")
system.add_vehicle(axio)
system.add_vehicle(prado)
system.register_customer(john)


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



# Testing part B of the rental.py system
print("-"* 50)
rental1 = system.rent_vehicle(john, prado, 4)
print(prado.is_available())             # False
print(len(system.rentals), len(john.rentals))   # 1 1

# Rule 6: renting the same car again
try:
    system.rent_vehicle(john, prado, 2)
except ValueError as error:
    print(f"Error: {error}")

# Rule 3: unregistered customer
stranger = Customer("C099", "Not Registered", "0700000000", "11111111", "DL00000")
try:
    system.rent_vehicle(stranger, axio, 2)
except ValueError as error:
    print(f"Error: {error}")

# Return late, car is freed
system.return_vehicle(rental1, actual_days=6)
print(prado.is_available())             # True
print(rental1.calculate_total())        # 37200

# Rule 8: returning twice
try:
    system.return_vehicle(rental1, actual_days=6)
except ValueError as error:
    print(f"Error: {error}")

    system.rent_vehicle(john, axio, 3)

# part c test
system.search_vehicles(vehicle_type="SUV")
system.search_vehicles(vehicle_type="SUV", max_daily_rate=6500)   # no SUVs under 6,500 in your fleet
system.search_vehicles(max_daily_rate=1000)                       # expect "no vehicles match"
try:
    system.search_vehicles(vehicle_type="Boat")
except ValueError as error:
    print(f"Error: {error}")

system.show_active_rentals()       # the Axio rental
system.show_completed_rentals()    # the Prado rental

from payment import MpesaPayment
from payment import CashPayment
from payment import CardPayment

print("-"*20)
payment = MpesaPayment(rental1, "0712345678")
print(payment.process_payment())

print("-"*20)
card_pay = CardPayment(rental1,"1020") 
print(card_pay.process_payment())

print("-"*20)
payment2 = CashPayment(rental1, 40000)
print(payment2.process_payment())  

print("-"*20)
payment3 = CashPayment(rental1, 20000)
print(payment3.process_payment())  #not enough cash # False


print("-"*20)
print(CardPayment(rental1, "1020").process_payment())     # Card ending 1020 charged KSh 37,200, then True

try:
    CardPayment(rental1, "4417 8888 1234 5678")           # a full number should be refused
except ValueError as error:
    print(f"Error: {error}")

print("-"*20)
from payment import Payment

try:
    Payment(rental1)                                       # abstraction: must fail
except TypeError as error:
    print(f"Error: {error}")

payment = MpesaPayment(rental1, "0712345678")
print(system.process_payment(payment))
print(system.revenue)
print(rental1.is_paid())


# 1. Paying twice must fail (rental1 is now paid)
try:
    system.process_payment(CashPayment(rental1, 40000))
except ValueError as error:
    print(f"Error: {error}")

# 2. An unreturned rental can't be paid
# active = system.rent_vehicle(john, axio, 2)
# try:
#     system.process_payment(MpesaPayment(active, "0712345678"))
# except ValueError as error:
#     print(f"Error: {error}")

# # 3. A failed payment changes nothing
# system.return_vehicle(active, actual_days=2)
# before = system.revenue
# print(system.process_payment(CashPayment(active, 100)))   # False
# print(system.revenue == before)                           # True
# print(active.is_paid())                                   # False

# 4. The bypass experiment
system.__revenue = 10_000_000
print(system.revenue)    

system.generate_report()      

print(axio.extra_charge(3))     # None
print(prado.extra_charge(3))    # ('Service Charge', 2000)
# print(merc.extra_charge(3))     # ('Insurance (10%)', 4500)
# 
from vehicle import EconomyCar, SUV, LuxuryCar
from customer import Customer
from rental import Rental

john = Customer("C001", "John Kamau", "0712345678", "12345678", "DL45821")

for car in [
    EconomyCar("T1", "Toyota", "Axio", 2022, 4000),
    SUV("T2", "Toyota", "Prado", 2023, 8000),
    LuxuryCar("T3", "Mercedes-Benz", "E-Class", 2024, 15000),
]:
    Rental("R900", john, car, 3).display_rental_details()                           # still the real figure