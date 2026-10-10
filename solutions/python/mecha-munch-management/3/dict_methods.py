"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    
    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
            
    return current_cart
    


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    return dict.fromkeys(notes,1) 


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    
    for recipe_key, recipe_value in recipe_updates:
        # if ideas[recipe_key] == recipe_key:
        ideas[recipe_key] = recipe_value
        # else:
            # ideas.update({recipe_key: recipe_value})
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.´
    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}
    for cart_item in cart:
        fulfillment_cart[cart_item] = ([cart[cart_item]] + aisle_mapping[cart_item] )

    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    new_store_inventory = {}
    for item, value in store_inventory.items():
        store_qty = value[0]
        aisle = value[1]
        fridge = value[2]
        if item in fulfillment_cart:
            new_store_quantity = store_qty - fulfillment_cart[item][0]

            if new_store_quantity == 0:
                new_store_quantity = 'Out of Stock'
        else:
            new_store_quantity = store_qty
        new_store_inventory[item] = [new_store_quantity, aisle, fridge]

    return new_store_inventory
   