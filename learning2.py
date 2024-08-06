# Car Price Checker

# Define product prices
bugatti = 50000000  # Price of Bugatti
renult = 21000    # Price of Renult

# Determine which product costs less and print the result
if bugatti < renult:
    print("Bugatti is less than Renult.")  # This will print if Bugatti is cheaper
elif renult < bugatti:
    print("Renult is less than Bugatti.")  # This will print if Renult is cheaper
else:
    print("Both cars have the same price.")  # This will print if both prices are equal
