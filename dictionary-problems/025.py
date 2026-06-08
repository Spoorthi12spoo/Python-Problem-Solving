#025.Given a dictionary of items and prices, find the total bill amount.

items = {'milk':40, 'bread':30, 'eggs':60}
total_bill=0
for item,price in items.items():
    total_bill+=price
print(total_bill)

