"""
Team Activity:  NUMBERS LIST

Compute the sum, or total, of the numbers in the list.

Compute the average of the numbers in the list.

Find the maximum, or largest, number in the list.

Have the user enter both positive and negative numbers, 
then find the smallest positive number (the positive number that is closest to zero).

Sort the numbers in the list and display the new, sorted
list. Hint: There are python libraries that can help you here, try searching the internet for them.
"""

# list set up
items = []
new_item = ""
#user info prompt
while new_item != "0":
    new_item = input('Please enter a list of numbers (type: 0 to finish): ')
    items.append(float(new_item))
print('Thank you!')
print()
#printing itesm
for item in items:
    print(f'Your item is {item}:  ')
print()
#the maths
print(f'THE MATHOMATICS: ')
#sum
print_sum = sum(items)
print()
print(f'The sum is: {print_sum}')
#average
print_average = sum(items) / len(items)
print()
print(f'The average is: {print_average}')
#Largest Number
print_largest = max(items)
print()
print(f'The largest is: {print_largest}')
#smallest + number
print_smallest =  1111 > min(items) >= 0
print()
print(f'The smallest positive number is: {print_smallest}')
#printed list in order!
print_sort = sorted(items)
print()
print('The sorted list is:')
for item in print_sort:
    print(item)