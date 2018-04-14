# get the price from the user
price = float(raw_input('Please enter the transaction price.\n'))

# get the amount given from the user
given = float(raw_input('Please enter the amount the customer gave.\n'))

change = (given - price) * 100  # Multiply by 100 to prevent imprecisions

ones = int(change / 100)
change %= 100
dimes = int(change / 10)
change %= 10
nickels = int(change / 5)
change %= 5
pennies = int(change)

print '\nChange:'
print str(ones) + ' $1 bills'
print str(dimes) + ' dimes'
print str(nickels) + ' nickels'
print str(pennies) + ' pennies'

raw_input('\nPress Enter to close...')
