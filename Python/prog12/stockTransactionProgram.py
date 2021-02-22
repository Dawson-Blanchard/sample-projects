# Did Joe make or loss money
# joe, broker, stock, variable

joe = 2000
stock = 40.00
broker = 0.03

# purchase price and payment ot broker

paid1 = joe * stock
paid2 = paid1 * broker

# amount when bought

print('amount paid for stock:$ ',paid1)
print('broker commission 1:$ ',paid2)


# price sold for and payment to broker

soldstock = 42.75
sold = joe * soldstock
paid3 = sold * broker

#  amount when sold

print('stock sold for:$ ',sold)
print('broker commission 2:$ ',paid3)

# net profit

total = paid2 + paid3
total1 = total + paid1
total2 = sold - total1

print('net profit:$ ',total2)
