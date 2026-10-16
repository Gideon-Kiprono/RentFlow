from abc import ABC, abstractmethod
import random, string

class Payment(ABC):
    def __init__(self, rental):
        self.rental = rental
        self.amount = rental.calculate_total()

        if self.amount <  0:
            raise ValueError("Payment amounts cannot be negative")
        


    @abstractmethod
    def process_payment(self):
        pass

class MpesaPayment(Payment):
    def __init__(self, rental, phone_number):
        super().__init__(rental)
        self.phone_number = phone_number


    def process_payment(self):
        code = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        print("Processing M-PESA payment....")
        print(f"Transaction: {code}")
        print(f"Payment of Ksh {self.amount:,} successful")
        return True

class CardPayment(Payment):
    def __init__(self, rental, last_four_digits):
        super().__init__(rental)
        self.last_four_digits = last_four_digits
        if not (str(self.last_four_digits).isdigit() and len(str(self.last_four_digits)) == 4):
            raise ValueError("Card must have exactly 4 digits.")
                
    def process_payment(self):
        print(f"Card ending {self.last_four_digits} charged Ksh {self.amount:,}")
        return True


class CashPayment(Payment):
    def __init__(self, rental, cash_given):
        super().__init__(rental)
        self.cash_given = cash_given


    def process_payment(self):
        
        if self.cash_given < self.amount:
            print("Not enough cash")
            return False
        else:
            change_due = self.cash_given - self.amount
            print(f"Cash Received : Ksh {self.cash_given:,}")
            print(f"Change due: Ksh {change_due:,}")
            print(f"Cash Payment of Ksh {self.amount:,} recorded")
            return True

        