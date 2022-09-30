"""Classes for melon orders."""


from email.mime import base
import random
########
from datetime import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None
    tax = 0
    

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = AbstractMelonOrder.get_base_price()

        if self.species == "Christmas":
            base_price = base_price * 1.5 


        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international":
            if self.qty < 10:
                total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price():
        """Get's random integer between 5 and 9 and returns it"""
        
        price = random.randint(5,9)
        
        now = datetime.now()
        today = now.date()
        weekday = today.weekday()
        current_time = now.time()
        hour = current_time.hour()
        

        if weekday in range(0,5) and hour in range(8,12):
            price += 4
            

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """An order made by the government"""
    order_type = "government"
    tax = 0

    def __init__(self, species, qty, passed_inspection = False):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.passed_inspection = passed_inspection

    def mark_inspection(self, passed):
        self.passed_inspection = passed