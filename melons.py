"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    def __init__(self, species, qty, country_code="US"):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.fee = 0

    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
            
        total = (1 + self.tax) * self.qty * base_price + self.fee

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True
    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
        

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        #Call the init method from parent class of DMO and set instance attributes with defaults from AMO
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)   
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

        if self.qty < 10:
            self.fee = 3.00
