cost = 16
tax_percent=.25
tax=cost*tax_percent
price=cost+tax
print('price', price)

# strings
username="nithinsamuel"
first_name='Nithin'
print(username+' '+first_name)

"""
Multiple line comments using three quotes
"""
"""
# Assignment # calculate tax
-You have $50
-You buy an item that is $15
-with a tax of 3%
-print how much money you have left
"""
moneyAvailable=50
tax=3
item=15

money_left=moneyAvailable - item-item*(tax/100)
print('money_left',money_left)
