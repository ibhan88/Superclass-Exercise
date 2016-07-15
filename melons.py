"""This file should have our order classes in it."""

from random import choice 


class AbstractMelonOrder(object):
    """This is our superclass"""

    def __init__(self, species, qty):
        """ initialize melon AbstractMelonOrder attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """ randomly choose base_price from 5-9 """

        random_base_price = choice(range(5,9))
        return random_base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "Christmas melon":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

 
    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.order_type = 'domestic'
        self.passed_inspection = False
        self.tax = 0

        super(GovernmentMelonOrder, self).__init__(species, qty)

    def mark_inspection(self, passed):
        """Mark inspection for True or False."""

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.order_type = "domestic"
        self.tax = 0.08

        super(DomesticMelonOrder, self).__init__(species, qty)

    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

        super(InternationalMelonOrder, self).__init__(species, qty)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
