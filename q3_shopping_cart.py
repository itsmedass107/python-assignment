#Part A - Spot the Bug

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print("Part A Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))



#Part B - Fix the Bug

def add_item_fixed(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)
    return cart

print("Part B Output:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))





