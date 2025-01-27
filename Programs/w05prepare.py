"""
        Madison Rollins
        W05 Prepare 
"""
"""
 List your friends
 
Type the name of a friend: Matthew
Type the name of a friend: Mark
Type the name of a friend: Luke
Type the name of a friend: John
Type the name of a friend: end

Your friends are:
Matthew
Mark
Luke
John
"""

"""
# list set up
friends = []
new_friend = ""
#user info prompt
while new_friend.lower() != "quit":
    new_friend = input('What are your friends')
    friends.append(new_friend)
print(f'Your friends are:')
for friend in friends:
    print(friend)
"""

"""
shopping list
Please enter the items of the shopping list (type: quit to finish):
Item: Milk
Item: Bread
Item: Candy
Item: Carrots
Item: quit

The shopping list is:
Milk
Bread
Candy
Carrots

The shopping list with indexes is:
0. Milk
1. Bread
2. Candy
3. Carrots

Which item would you like to change? 2
What is the new item? Apples

The shopping list with indexes is:
0. Milk
1. Bread
2. Apples
3. Carrots
"""

# list set up
items = []
new_item = ""
#user info prompt
while new_item.lower() != "quit":
    new_item = input('Please enter the items of the shopping list (type: quit to finish): ')
    items.append(new_item)
#print items
print(f'The shopping list with indexes is: ')
for item in items:
    print(item)
#index set up
number_of_items = len(items)
#print index
for i in range(len(items)):
    print()
    print('')
    book = items[i]
    print(f"{i}. {item}")
#changing item based on index
print()
change = input('Would you like to change an item?  ')
if change.lower() == "no":
    print('Okay!  Have a good day!')
else:
    print()
    index = input('Which item would you like to change? ')
    new_item = input("What is the new item? ")
    items.append[index] = new_item
    print()
    print(f'The shopping list with indexes is: ')
    for item in items:
       print(item)
