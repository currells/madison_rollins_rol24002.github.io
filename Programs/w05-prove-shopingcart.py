"""
    Madison Rollins
    Shopping Cart

Add a new item

Display the contents of the shopping cart

Remove an item (only needed for the final project deliverable)

Compute the total (only needed for the final project deliverable)

Quit


"""
# list set up
items = []
new_item = ""
prices = []
new_price = []
items_and_prices = [] 
#user info promptmilk
while new_item.lower() != "quit":
    new_item = input('Please enter the items on the shopping list (type: quit to finish): ')
    if new_item.lower() == "quit":
        break  # Exit the loop
    else:
        new_price = float(input('What is the Price?: '))
        items.append(new_item)
        prices.append(new_price)
        # Ensure both variables have values
    if new_item and new_price: 
        items_and_prices.append((new_item, new_price))
        print(f"'{new_item}' added to the cart for ${new_price:.2f}")
#print items
print()
print()
print(f'The items on your list are: ')
number_of_items = len(items)
for i in range(len(items)):
    print()
    item = items[i]
    price = prices[i]
    print(f"{i+1}. {item} - ${price:.2f}")

#changing item based on index
print()
change = input('Would you like to change an item?  ')
if change.lower() == "no":
    total = sum(prices)
    print(f'The total price of the items in the shopping cart is ${total:.2f}')
else:
    print()
    index = int(input('Which item would you like to change? '))
    new_item = input("What is the new item? ")
    new_price = float(input('What is the Price?: '))
    prices[index] = new_price
    items[index] = new_item
    items_and_prices[index] = (new_item, new_price)
    print()
print(f'The items on your list are: ')
number_of_items = len(items)
for i in range(len(items)):
    print()
    item = items[i]
    price = prices[i]
    print(f"{i+1}. {item} - ${price:.2f}")
    print()
    print(f'The total price of the items in the shopping cart is ${total:.2f}')
