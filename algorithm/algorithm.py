# Function that finalizes shopping in a web store
# Input:
# shopping_list: dictionary {key=product: value=quantity-client-wants-to-buy}
# storage: dictionary {key=product: value: [quantity-at-store, price]}
def finalize_shopping_cart(shopping_list, storage):
    # Amount that will be calculated
    amount = 0
    # Empty cart that will be filled with products to buy
    cart = []

    # The algorithm iterates through every product on the user's list
    for item in shopping_list.keys():
        # Checks if the product is in the store and the quantity is sufficient
        # if so it adds the product to the basket, updates the amount to pay and updates the shop's storage
        if item in storage.keys() and shopping_list[item] <= storage[item][0]:
            cart.append(item)
            amount += storage[item][1] * shopping_list[item]
            storage[item][0] -= shopping_list[item]
            if storage[item][0] == 0:
                storage.pop(item)
        # If the product is in the shop but the quantity is too small
        # it adds only the available quantity and informs client about it
        elif item in storage.keys():
            print("Sorry, there's not enough ", item, " only ", storage[item][0], " will be added to your cart")
            cart.append(item)
            amount += storage[item][0] * storage[item][1]
            storage.pop(item)
        # Else if the product is not in the shop at all it give the information to client and doesn't add it to the cart
        else:
            print("Sorry, we don't have ", item, " in our storage")

    print("Here is your basket ", cart)
    # amount client will pay for available products
    return round(amount, 2), cart, storage


if __name__ == '__main__':
    # list = {product: quantity-client-wants-to-buy}
    shopping_list1 = {"apple": 13, "banana": 1, "milk": 2, "cookies": 2, "paper": 3}
    # store = {product: [quantity-at-store, price]}
    store = {"apple": [10, 1.5], "banana": [2, 2.1], "milk": [20, 1.3], "cookies": [130, 13.4], "paper": [100, 10.2],
             "juice": [102, 2.4]}
    result, basket, store = finalize_shopping_cart(shopping_list1, store)
    print(result)
    print(store)
