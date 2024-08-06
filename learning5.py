# Prompt the user to enter their choice
choice = int(input("Enter your choice (1-5): "))  # Get the user's choice

# Perform the selected string manipulation based on user choice
if choice == 1:
    result = input_string.upper()  # Convert the string to uppercase
    print("Uppercase:", result)    # Print the uppercase string
elif choice == 2:
    result = input_string.lower()  # Convert the string to lowercase
    print("Lowercase:", result)    # Print the lowercase string
elif choice == 3:
    start = int(input("Enter start index: "))  # Get the start index from the user
    end = int(input("Enter end index: "))      # Get the end index from the user
    result = input_string[start:end]           # Slice the string from start to end index
    print("Sliced string:", result)            # Print the sliced string
elif choice == 4:
    length = len(input_string)  # Calculate the length of the string
    print("String length:", length)  # Print the string length
elif choice == 5:
    print("Characters:")  # Print header for characters
    for char in input_string:  # Loop through each character in the string
        print(char)  # Print each character
else:
    print("Invalid choice.")  # Print an error message for an invalid choice