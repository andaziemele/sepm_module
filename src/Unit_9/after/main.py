
"""
Main component of the cupboard script.

# what is left to do:
# create flowcharts and add into new assignment - done
# add structure to new assignment - done
# write new assignment - done
# add references to new assignment - done
# refine new assignment - done
# add app flowchart - done
# comment main run script blocks - done
# finish remove item interface - done
# finish search item interface - done
# finalise type hints - done
# check for right docstring formatting - done
# finalise all comments - done
# fix empty inputs for input item - done
# add pre-defined categories prompt - done
# add tests for:
# valid date input - done
# valid quant input - done
# changes to item length - done
# search for item - done
"""
from project.cupboard import Cupboard
from project.item import Item

# launch Python script
if __name__ == "__main__":
    # initialise new Cupboard object
    cupboard = Cupboard()
    # main screen input prompt
    x = int(
        input(
            "Welcome to your food cupboard! What would you like to do? Enter the number and press ENTER on your keyboard. \n \
                [1] Insert a new item \n \
                [2] Search for an existing item \n \
                [3] Sort and view existing items \n \
                [4] Remove an existing item \n \
                [5] Leave app \n"
        )
    )

    # app will continue running as long as inputs are valid and user selection ranges between options 1-4
    # key actions are only associated with user options 1 to 4
    while x in range(1, 5):
        # "input item" user option
        if x == 1:
            # assign cupboard length for assertion test
            n = len(cupboard)
            # item name input (str)
            item_name = input(
                "What is the name of the item? Press ENTER when you're finished typing.\n"
            )
            # item category input selection (int)
            item_category = input(
                "What is the category of the item? Enter Category number and press ENTER.\n \
                            [1] Pasta, Rice and Pulses \n \
                            [2] Canned Vegetables \n \
                            [3] Tea, Coffee and Long-life \n \
                            [4] Spices and Other Meal Ingredients \n \
                            [5] Cereals, Muesli and Granola \n \
                            [6] Other \n"
            )
            # selecting "Other" will allow own custom category inputs
            if item_category == "6":
                item_category = input("What is the category of this item? \n")
            # optional item date input (str)
            item_date = input(
                "(Optional: Press ENTER to skip.) When does the item expire (YYYY-MM-DD)? \n \
                                Press ENTER when you're ready.\n"
            )
            # optional item quantity input (int)
            item_quantity = input(
                "(Optional: Press ENTER to skip.) How many of these items do you have? \n \
                                    Press ENTER when you're ready.\n"
            )
            new_item = Item(item_name, item_category, item_date, item_quantity)
            # validate item inputs and insert the new item if successful
            new_item = cupboard.validate_item_inputs(new_item)
            cupboard.insert_item(new_item)
            # assertion test to check if item has been added via Cupboard object length increasing by one
            assert len(cupboard) == n + 1
            # search for the new item in cupboard
            test_findings = cupboard.search_item(item=new_item)
            # assertion test to check if search_item yields items
            assert test_findings
            print("Item successfully added!")
            # follow up with next input prompt
            x = int(
                input(
                    "What would you like to do next? Enter the number and press ENTER on your keyboard. \n \
                [1] Insert new item \n \
                [2] Search for an item \n \
                [3] Sort and view items \n \
                [4] Remove an item \n \
                [5] Leave app \n"
                )
            )
        # "search item" user option
        if x == 2:
            # search term input (str)
            search_term = input(
                "What would you like to search for? Press ENTER when you're ready.\n"
            )
            # search type input (str)
            search_type = input(
                "Where would you like to search in: item \n \
                                [1] Name \n \
                                [2] Category? \n \
                                Press ENTER when you've finished typing.\n"
            )
            # set up inputs for search
            if search_type in ["1", "name", "Name", "NAME"]:
                search_type = "name"
            elif search_type in ["2", "category", "Category", "CATEGORY"]:
                search_type = "category"
            else:
                search_type = "name"
            # search for item
            findings = cupboard.search_item(search_term, search_type)
            # if list not empty
            if findings:
                print("I found these items!")
                found_items = [str(cupboard[i]) for i in findings]
                print(found_items)
            else:
                print("I didn't find anything matching your search term!")
            x = int(
                input(
                    "What would you like to do next? Enter the number and press ENTER on your keyboard. \n \
                            [1] Insert new item \n \
                            [2] Search for an item \n \
                            [3] Sort and view items \n \
                            [4] Remove an item \n \
                            [5] Leave app \n"
                )
            )
        # "sort and view item" user option
        if x == 3:
            # sort type input
            sort_type = int(
                input(
                    "How would you like to sort? Enter the number and press ENTER on your keyboard. By: \n \
                            [1] Name \n \
                            [2] Category \n \
                            [3] Date \n \
                            [4] Quantity \n"
                )
            )
            # assign Item attribute name to sort type based on user selection
            if sort_type == 1:
                sort_type = "name"
            elif sort_type == 2:
                sort_type = "category"
            elif sort_type == 3:
                sort_type = "date"
            elif sort_type == 4:
                sort_type = "quant"
            else:
                sort_type = "name"
            # bubble sort, taking attribute name
            sorted_items = cupboard.bubble_sort(sort_type)
            # create and print human-readable output
            # noinspection PyRedeclaration
            sorted_items = cupboard.view_cupboard()
            print(sorted_items)
            x = int(
                input(
                    "What would you like to do next? Enter the number and press ENTER on your keyboard. \n \
                                        [1] Insert new item \n \
                                        [2] Search for an item \n \
                                        [3] Sort and view items \n \
                                        [4] Remove an item \n \
                                        [5] Leave app \n"
                )
            )
        # "remove item" user option
        if x == 4:
            # user input for searching the removal item first
            removal_term = input(
                "Input search term for item to remove. Press ENTER when you're ready.\n"
            )
            # search will be done based on name by default
            findings = cupboard.search_item(removal_term, "name")
            # if search results exist
            if findings:
                # assign cupboard length for assertion test
                n = len(cupboard)
                print("I found these items!")
                # print full item details with their original indices
                found_items = [("Item " + str(i), str(cupboard[i])) for i in findings]
                print(found_items)
                # prompt user to input item index
                remove_index = int(
                    input(
                        "Which item would you like to remove? Enter the number next to 'Item'. \n"
                    )
                )
                remove_prompt = input(
                    "You will remove {item}. Is this correct? Enter the number of option. \n \
                                          [1] Yes \n \
                                          [2] No \n".format(
                        item=str(cupboard[remove_index])
                    )
                )
                if remove_prompt in [
                    "1",
                    "Yes",
                    "y",
                    "yes",
                    "Y",
                    "YES",
                ]:  # to allow for multiple accidental user entries
                    print("Removing Item", remove_index, "...")
                    # remove item and save for later testing
                    removal_item = cupboard.remove_item(remove_index)
                    # quick assertion test to check if item has been removed via Cupboard object length reducing by one
                    assert len(cupboard) == n - 1
                    # try to locate the user-selected item to remove
                    test_findings = cupboard.search_item(item=removal_item)
                    # assert will fail if incorrect item removed
                    assert not test_findings
                    print("Item successfully removed!")
                else:
                    print("Let's try again.")
            else:  # inform user nothing has been found and prompt next action
                print("I didn't find anything matching your search term!")
            x = int(
                input(
                    "What would you like to do next? Enter the number and press ENTER on your keyboard. \n \
                                                    [1] Insert new item \n \
                                                    [2] Search for an item \n \
                                                    [3] Sort and view items \n \
                                                    [4] Remove an item \n \
                                                    [5] Leave app \n"
                )
            )
