# Prompt the user for input
first_name = input("Enter your first name: ")  # Get the first name from the user
last_name = input("Enter your last name: ")    # Get the last name from the user
age = input("Enter your age: ")                # Get the age from the user
city = input("Enter your city: ")              # Get the city from the user
occupation = input("Enter your occupation: ")  # Get the occupation from the user

# Concatenate first name and last name
full_name = first_name + " " + last_name  # Combine first and last names to form the full name

# Create profile description using string formatting
profile_desc = f"{full_name} is {age} years old, lives in {city}, and works as a {occupation}."  # Format the profile description

# Add escape characters to include quotation marks and a new line
profile_info = "\"Profile Information:\"\n" + profile_desc  # Add quotes and a newline to the profile description

# Use string methods to modify the full name and profile description
modified_name = full_name.upper()  # Convert the full name to uppercase
# Replace 'a' with 'an' if the occupation starts with a vowel
if occupation[0].lower() in "aeiou":
    modified_desc = profile_info.replace(" a ", " an ")
else:
    modified_desc = profile_info

# Display the user profile
print("===== User Profile =====")  # Print the profile header
print(modified_name)              # Print the modified full name
print(modified_desc)              # Print the modified profile description
print("========================")  # Print the profile footer