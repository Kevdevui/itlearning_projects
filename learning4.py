# 1. Import random module
import random  # Importing the random module to generate random numbers

# 2. Generate random number between 1 and 100
random_number = random.randint(1, 100)  # Generate a random number between 1 and 100

# 3. Print random number with its data type using type() function
print(">---------------------------------------<")  # Print the top border
print("Random Number:", random_number)             # Print the random number
print("Data Type:", type(random_number))           # Print the data type of the random number
print(">---------------------------------------<")  # Print the bottom border

# 4. Multi-word variables conventions such as camel case, pascal case, or snake case
multiWordVariableCamelCase = "ThisIsCamelCase"        # Example of camel case
multiWordVariablePascalCase = "ThisIsPascalCase"      # Example of pascal case
multi_word_variable_snake_case = "this_is_snake_case" # Example of snake case

# Type conversion examples by converting the random number to a float and then to a complex number
float_number = float(random_number)  # Convert the random number to a float
complex_number = complex(random_number)  # Convert the random number to a complex number

# Print the converted numbers with their data types
print(">---------------------------------------<")  # Print the top border for float conversion
print("Random Number as Float:", float_number)     # Print the random number as a float
print("Data Type after Conversion to Float:", type(float_number))  # Print the data type of the float number
print(">---------------------------------------<")  # Print the bottom border for float conversion

print(">---------------------------------------<")  # Print the top border for complex conversion
print("Random Number as Complex:", complex_number)  # Print the random number as a complex number
print("Data Type after Conversion to Complex:", type(complex_number))  # Print the data type of the complex number
print(">---------------------------------------<")  # Print the bottom border for complex conversion
