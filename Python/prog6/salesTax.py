# Get purchase price
# price, state, county, variable

price = float(input('Enter purchase price: '))
state = 0.05
county = 0.025

# Calculate the total amount
# and add sales tax

total1 = (price * state)
total2 = (price * county)
total3 = (total1 + total2)
total4 = (price + total3)

# Displays state and county tax, total tax, and final amount

print('state tax is: ',total1)
print('county tax is: ',total2)
print('total tax is: ',total3)
print('The total amount is: ',total4)