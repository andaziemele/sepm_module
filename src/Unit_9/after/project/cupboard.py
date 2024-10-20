
"""
Main Cupboard module for storing the Cupboard class.

Contains multiple necessary classes.
"""


class Cupboard:
    """
    The class for storing Item objects.

    It also stored associated functions for:
    * Searching items
    * Sorting items
    * Inserting items
    * Removing items
    * Displaying items back to the user.
    """

    def __init__(self):
        """Cupboard initialised as an empty list."""
        self._items = []

    def __len__(self):
        """Built-in function for returning length of Cupboard list."""
        return len(self._items)

    def __getitem__(self, item: int):
        """
        Built-in function for indexing Cupboard list.

        :param item: index of required item
        """
        return self._items[item]

    # def __index__(self):

    def insert_item(self, item: object):
        """
        Insert Item object in Cupboard list.

        :param item: object
        """
        self._items.append(item)

    def search_item(self, keyword: str = None, attr: str = None, item: object = None):
        """
        Sequential search for Item(s) in Cupboard list.

        This is based on:
        1. search keyword and Item attribute (name or category), or
        2. full Item object.
        :param keyword: search keyword
        :param attr: what field to search in: name or category
        :param item: Item object to search for
        :return indices: list of indices found
        """
        # set empty list where to store matching results
        indices = []
        # loop through the items in the Cupboard
        if attr:  # if attribute in which to search has been specified by user
            for i in range(len(self._items)):
                # lowercase both keyword and attribute strings to optimize search results
                if keyword.lower() in getattr(self._items[i], attr).lower():
                    # append to end of indices list if keyword in Item attribute
                    indices.append(i)
        else:  # this search type is used for remove function testing purposes
            for i in range(len(self._items)):
                # check item equality
                if item == self._items[i]:
                    # append to end of indices list if Item found
                    indices.append(i)
        # return list of match indices
        return indices

    def binary_search(self, search_item: object):
        """
        Binary search for Item objects in Cupboard list to locate full Item object.

        :param search_item: Item object
        """

        def split(tree):
            """
            Help in splitting tree at root node.

            :param tree: list of items in tree to be split
            """
            # set middle index for root
            root_index = len(tree) // 2
            root_node = tree[root_index]
            # get children on the left of root
            first_half = tree[0:root_index]
            # get children on the right of root
            second_half = tree[root_index + 1 : len(tree)]
            # return root node, left and right children for further splitting if required
            return root_node, first_half, second_half

        # assign length of item list to n for iterating through the tree and use bubblesort
        ns = len(self._items)
        items = self.bubble_sort()
        while ns > 0:
            if items:  # if item not found and searching continues
                root_item, first_set, second_set = split(items)
            else:  # if items exhausted and still no match, item does not exist in tree
                print("Search item does not exist.")
                return []
            if (
                search_item < root_item
            ):  # given items are sorted, item will be searched in left children
                items = first_set
            elif (
                search_item > root_item
            ):  # given items are sorted, item will be searched in right children
                items = second_set
            else:  # search item is node item
                print(
                    "Found {search_item} at iteration {n}.".format(
                        search_item=search_item, n=ns
                    )
                )
                return search_item
            # reduce number of iterations needed
            ns = ns - 1

    def bubble_sort(self, attr: str):
        """
        Implement the bubble sort algorithm.

        :param attr: Item attribute to use for sorting
        :return self._items: sorted Cupboard items
        """
        # assign length of input list to variable nb to set number of total loops
        nb = len(self._items)
        while nb > 0:
            # set counter at 0 to capture 0th index position in list
            counter = 0
            # loop through each individual item in input list
            for i in self._items:
                # conditional to control for when index exceeds input length
                if len(self._items) > counter + 1:
                    # if item at current index position is greater than item at next (+1) index position
                    if getattr(i, attr) > getattr(self._items[counter + 1], attr):
                        # swap item at current index with item at next (+1) index position
                        self._items[counter] = self._items[counter + 1]
                        # swap item at next (+1) index position with item at current position
                        self._items[counter + 1] = i
                    # set counter to move onto next position
                    counter += 1
            # reduce number of loops by 1
            nb = nb - 1
        return self._items

    def remove_item(self, index: int):
        """
        Remove item at index and return it.

        :param index: index of item to be removed from Cupboard list
        :return removed_item: item removed from list
        """
        removed_item = self._items.pop(index)
        return removed_item

    def view_cupboard(self):
        """
        Return a human-readable list of all items available in cupboard.

        :return full_cupboard: a list of tuples, containing item index and item
        """
        full_cupboard = [
            ("Item " + str(ind), str(i)) for ind, i in enumerate(self._items)
        ]
        return full_cupboard

    @staticmethod
    def validate_item_inputs(item: object):
        """
        Validate inputs to add Item object.

        :param item: input Item object
        """

        def test_item_date_format(item_n: object):
            """
            Helper function to clean and validate Item date format when inputted.

            The output is not necessarily valid in real life, as February 31st (02-31)
            does not exist. In normal circumstances the datetime library would be used
            to handle the correct month-day relationships.
            :param item_n: Item object with its attributes
            :return item: Item object
            """
            # strip from any accidental leading/trailing whitespace entered by user
            date = item_n.date.strip()
            # YYYY-MM-DD should be 10 characters in total
            if len(date) != 10:
                raise ValueError(
                    "You must enter date in format YYYY-MM-DD, so 2024-05-04."
                )
            else:
                # check for the valid year range in the first four characters
                if (int(date[0:4]) < 1999) | (int(date[0:4]) > 2050):
                    raise ValueError(
                        "Your expiry year is out of range, expected 1999-2050."
                    )
                # check for the valid month range in the MM characters (1 to 12, so range -1)
                if int(date[5:7]) in range(1, 13):
                    # check for the valid day range in the DD characters (1 to 31, so range -1)
                    if int(date[8:10]) in range(1, 32):
                        pass
                    else:
                        raise ValueError("Your expiry day is invalid, expected 1-31.")
                else:
                    raise ValueError("Your expiry month is invalid, expected 1-12.")
            # return the validated date to be replaced as date attribute for Item
            return date

        # multiple if/else conditionals for testing
        if item.name:  # check if name exists/is not NaN, continue
            pass
        else:
            # ValueError, due to empty, inappropriate, unexpected entry
            raise ValueError("You must enter the item name!")
        if item.category:  # check if category exists/is not NaN, continue
            if item.category == "1":
                item.category = "Pasta, Rice and Pulses"
            elif item.category == "2":
                item.category = "Canned Vegetables"
            elif item.category == "3":
                item.category = "Tea, Coffee and Long-life"
            elif item.category == "4":
                item.category = "Spices and Other Meal Ingredients"
            elif item.category == "5":
                item.category = "Cereals, Muesli and Granola"
            elif isinstance(item.category, str):  # custom user string input
                item.category = item.category
            else:
                item.category = "Other"
        else:
            # ValueError, due to empty, inappropriate, unexpected entry
            raise ValueError("You must enter the item category!")
        if item.date:  # if user enters item_date, continue
            # validate date format
            new_date = test_item_date_format(item)
            item.date = new_date
        else:  # otherwise assign default date "2050-01-01"
            item.date = "2050-01-01"
        try:  # to account for blank entries
            # if user enters item_quantity, is an integer and bigger than 0, continue
            if (isinstance(int(item.quant), int)) & (int(item.quant) > 0):
                # ensure quant attribute is an int at all times
                item.quant = int(item.quant)
            else:  # otherwise assign default quantity 1
                print("Item quantity set to 1.")
                item.quant = 1
        except ValueError:  # due to blank entry
            print("Item quantity set to 1.")
            item.quant = 1
        # insert Item object in cupboard
        return item
