# Create a list of test scores
scores = [98, 92, 78, 50, 88]  # List of scores

# Calculate the average score using floor division
total_score = sum(scores)  # Sum all scores
num_tests = len(scores)  # Count the number of tests
average_score = total_score // num_tests  # Calculate the average score using floor division

# Determine the grade using comparison operators
if average_score >= 90:
    grade = "A"  # Grade A for scores 90 and above
elif average_score >= 80:
    grade = "B"  # Grade B for scores 80 and above
elif average_score >= 70:
    grade = "C"  # Grade C for scores 70 and above
elif average_score >= 60:
    grade = "D"  # Grade D for scores 60 and above
else:
    grade = "F"  # Grade F for scores below 60

# Update the grade using assignment operators
if average_score % 10 >= 5:
    grade += "+"  # Append a plus sign if the last digit of the average score is 5 or more

# Check if a specific score exists in the list using membership operators
check_score = 90  # Score to check
if check_score in scores:
    print(f"The score {check_score} exists in the list.")  # Confirm the score exists
else:
    print(f"The score {check_score} does not exist in the list.")  # Confirm the score does not exist

# Compare objects using identity operators
scores_copy = scores  # Create a reference to the same list
if scores is scores_copy:
    print("The scores and scores_copy are the same object.")  # Confirm they are the same object
else:
    print("The scores and scores_copy are different objects.")  # Confirm they are different objects

# Perform bitwise operations on the scores
bitwise_result = scores[0] & scores[1]  # Perform bitwise AND on the first two scores
print(f"Bitwise AND of the first two scores: {bitwise_result}")  # Display the result of the bitwise AND operation

# Display the student's grade
print(f"The student's average score is {average_score} and their grade is {grade}.")  # Display the average score and grade
