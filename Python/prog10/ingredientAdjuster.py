# Calculate number of ingredients per cups
# sugar, butter, flour, amount, variable

amount = float(input('How many cookies do you want: '))
cookies = 48
sugar = 1.5
butter = 1
flour = 2.75

# Find the amount of ingredients

total1 = amount / cookies
total2 = total1 * sugar
total3 = total1 * butter
total4 = total1 * flour

# Diplays change in number of ingredients

print('cups of sugar: ',format(total2, '.2f'))
print('cups of butter:',format(total3, '.2f'))
print('cups of flour:',format(total4, '.2f'))


