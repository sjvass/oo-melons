"""Classes for melon orders."""
class AbstractMelonOrder():
    """A abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", tax=0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international melon order."""
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", tax=0.17)
        self.country_code = country_code

    def get_total(self):
        """Overridden get_total method including international flat fee"""
        return (super().get_total() + 3 if self.qty < 10
         else super().get_total())

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order for the US goverment"""

    #true if order has passed inspection
    passed_inspection = False

    def __init__(self, species, qty):
        super().__init__(species, qty, "goverment", tax=0)

    def mark_inspection(self, passed):
        """updates passed_inspection to value of boolean passed"""
        self.passed_inspection = passed





# class DomesticMelonOrder():
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder():
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code
