"""This file should have our order classes in it."""

from random import randint

# Parent class for melon orders. No class-level attributes.
class AbstractMelonOrder(object):

    # Constructor method. Initializes instance attributes to the values
    # passed by the user, or defaults as appropriate.
    def __init__(self, species, qty, country_code="US"):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.fee = 0

    # Choose base price randomly for splurge pricing. 
    def get_base_price(self):
        return randint(5,9)

    #Method calculates the total for melon order. Fee defaults to 0 unless
    #a fee is applied in a later method. 
    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        #Checks to see if the melon being ordered is a Christmas Melon. If so, 
        #Sets the base_price to 1.5 times the orgininal base_price. 
        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
        #Calculates the total using the tax (individually defined), quantity, 
        #base_price and fee. 
        total = (1 + self.tax) * self.qty * base_price + self.fee
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True
    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
        
# A subclass, DomesticMelonOrder, that inherits from AbstractMelonOrder.
class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        # Call the init method from parent class of DomesticMelonOrder and set instance 
        # attributes with defaults from AbstractMelonOrder.
        super(DomesticMelonOrder, self).__init__(species, qty)

        # Set order_type to domestic and tax to 0.08. This is specific to 
        # domestic melon orders. 
        self.order_type = "domestic"
        self.tax = 0.08

class GovernmentMelonOrder(DomesticMelonOrder):
    """A domestic (in the US) melon order specifically for the US government."""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder,self).__init__(species,qty)
        self.tax = 0.0
        self.inspected = False
        #Made inspection_result none to indicate that it has not been inspected yet. 
        #Making it false was too ambiguous, can't tell if it failed or never inspected.
        self.inspection_result = None 

    # Part 3 solution based on instructions: 
    #   self.passed_inspection = False

    # def mark_inspection(self, passed):
    #     self.passed_inspection = passed

    #Modified Part 3 solution
    def mark_inspection(self,result):
        #Takes the user's input for "result" and assigns it to instance attr
        #self.inspection_result. Marks the instance attr of self.inspected to True.
        self.inspection_result = result
        self.inspected = True

# A subclass, InternationalMelonOrder, that inherits from AbstractMelonOrder.
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        # Call the init method from parent class of InternationalMelonOrder and set
        # instance attributes with defaults from AbstractMelonOrder. 
        super(InternationalMelonOrder, self).__init__(species, qty) 
        # Set order_type to international and tax to 0.17. This is specific to 
        # international melon orders.
        # Takes the country_code from the call of InternationalMelonOrder. 
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

        #If the quantity of the order is less than 10 melons, then the fee is set to
        # $3.00, overriding the default of $0. 
        if self.qty < 10:
            self.fee = 3.00

