"""
        Madison Rollins
        Meal Price Caclculator
            I added a tip funcion and gave the total it's own space.  
            The tip functions like the sales tax and the two are added to the subtotal to give the new total.
"""
""" number of meals
        Ask the user for the following:
            The price of a child's meal (floating point)
            The price of an adult's meal (floating point)
            The number of children (integer)
            The number of adults (integer)
        Then, complete the following steps:
            Determine the meal's subtotal (before adding sales tax) by multiplying
            the number of children by the price of their meal and multiplying the number 
            of adults by the price of their meal and adding those two values together.
        Display the subtotal.
"""
# title
print('Meal Price Calculator')
print()
print()
print('-----------')
#input info
print('Please Submit the Following:')
print()
child_meal = input('Price of childs meal:')
print()
adult_meal = input('Price of adult meal:')
print()
child_num = input('Number of children:')
print()
adult_num = input('Number of Adults:')
#math :)
child_price = (float(child_meal) * int(child_num))
adult_price = (float(adult_meal) * int(adult_num))
#subtotal
subtotal = (float(child_price) + float(adult_price))
print()
print('-----------')
#sub- print
print(f'The Subtotal is ${subtotal: .2f}')
print()
print('-----------')
""" Total Calculations
Ask the user for the sales tax rate as a percentage (floating point). 
Please note that this percentage should be entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.

Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.

Compute and display the total price of the meal by adding the subtotal and the sales tax.
"""
print()
print('Please Submit the Following:')
print()
#ask tax
tax = input('Enter the sales tax:')
#math
sales = ((float(tax)/100) * float(subtotal))
print()
#prints
print(f'Sales Tax: ${sales: .2f}')
print()
s
""" Adding Tip
"""
print('-----------')
print()
print('Please Submit the Following:')
print()
#moolah
tip_percent = input('Tip percentage:')
#math
tip = ((float(tip_percent)/100) * float(subtotal))
print()
print(f'Tip: ${tip: .2f}')
print()
print('-----------')
print()
print()
""" TOTAL """
print('-----TOTAL-----')
#math
total = (float(sales) + float(subtotal) + float(tip))
#ptitn
print()
print(f'Your Total is ${total: .2f}')
print()
""" Change 
Ask the user for the the payment amount (floating point)

Compute and display the change.
"""
print('-----------')
print()
print('Please Submit the Following:')
print()
#moolah
bill = input('Total of cash given:')
#math
change = (float(bill) - float(total))
print()
print(f'Your change is ${change: .2f}')
print()
print('-----------')