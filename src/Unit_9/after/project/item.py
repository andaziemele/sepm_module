class Item:
    """Class to create an Item object.
    Attributes:
    name: name of Item object, for example "penne pasta 500g"
    category: one of 5 pre-defined categories selected by user
    date: expiry date of item in ISO 8601 format, YYYY-MM-DD, for example, 2050-12-31
    quant: quantity of items
    """

    def __init__(
        self, name: str, category: str, date: str = "2050-01-01", quant: int = 1
    ):
        """
        Initialise Item object.
        Default input values are set for date and quant (quantity).
        :type name: str
        :type category: str
        :type date: str
        :type quant: int
        """
        self.name = name
        self.category = category
        self.date = date
        self.quant = quant

    def __str__(self):
        """Override of the built-in str to
        return a human-readable format of Item object and its fields."""
        # initialised when printing an Item object
        # for example, "1 Can of chopped tomatoes, under category "Canned vegetables" expiring on 2050-10-01"
        return f"{self.quant} {self.name.upper()}, under category {self.category.upper()} expiring on {self.date}."
