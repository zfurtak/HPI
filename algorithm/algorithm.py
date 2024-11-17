def finalize_shopping_cart(shopping_list, storage):
    amount = 0
    basket = []

    for item in shopping_list.keys():
        if item in storage.keys() and shopping_list[item] <= storage[item][0]:
            basket.append(item)
            amount += storage[item][1] * shopping_list[item]
            storage[item][0] -= shopping_list[item]
        elif item in storage.keys():
            print("Sorry, there's not enough ", item)
        else:
            print("Sorry, we don't have ", item, " in our storage")

    print("Here is your basket ", basket)
    # amount client will pay for available products
    return round(amount, 2), basket, storage


if __name__ == '__main__':
    # list = {product: quantity-client-wants-to-buy}
    shopping_list1 = {"apple": 13, "banana": 1, "milk": 2, "cookies": 2, "paper": 3}
    # store = {product: (quantity-at-store, price)}
    store = {"apple": [10, 1.5], "banana": [2, 2.1], "milk": [20, 1.3], "cookies": [130, 13.4], "paper": [100, 10.2],
             "juice": [102, 2.4]}
    result, basket, store = finalize_shopping_cart(shopping_list1, store)
    print(result)
    print(store)
