# Web Store Checkout Function 🛒

This function helps you manage online shopping carts by processing customer orders against available inventory, updating the inventory, and calculating the total cost.

## Features 🌟
- **Dynamic Inventory Updates:** Adjusts store inventory based on customer purchases.
- **Cost Calculation:** Automatically calculates the total price for the cart contents.
- **User Notifications:** Informs customers if an item's stock is insufficient or unavailable.

## Usage 🛍️
Input requires two dictionaries:
1. `shopping_list`: Products and desired quantities (e.g., `{'apple': 5, 'bread': 2}`).
2. `storage`: Products, their available quantities, and prices at the store (e.g., `{'apple': [10, 0.50], 'bread': [3, 1.20]}`).

### Example usage:
```python
shopping_list = {'apple': 5, 'bread': 2}
storage = {'apple': [10, 0.50], 'bread': [3, 1.20]}

total_amount, cart, updated_storage = finalize_shopping_cart(shopping_list, storage)
```
**Output**:
```
Here is your basket ['apple', 'bread']
```
