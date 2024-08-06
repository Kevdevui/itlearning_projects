# Create tuples for student records
student1 = ("Alice Brown", 19, "Grade 13")  # Student 1 record
student2 = ("Bob White", 18, "Grade 12")  # Student 2 record
student3 = ("Charlie Green", 17, "Grade 11")  # Student 3 record

# Create a tuple of student records
students = (student1, student2, student3)  # Tuple containing all student records

# Use tuple methods to get information
print(f"Number of students: {len(students)}")  # Print the number of students
print(f"Index of Bob White: {students.index(student2)}")  # Print the index of student2 (Bob White)

# Create sets for student IDs and courses
student_ids = {2001, 2002, 2003, 2004, 2005}  # Set of student IDs
courses = {"Biology", "Chemistry", "Physics", "Mathematics"}  # Set of courses

# Perform set operations to manage IDs and courses
print(f"Student IDs: {student_ids}")  # Print the set of student IDs
print(f"Courses: {courses}")  # Print the set of courses

# Add new student IDs to the existing set
new_students = {2006, 2007}  # Set of new student IDs
student_ids.update(new_students)  # Update the student_ids set with new students
print(f"Updated Student IDs: {student_ids}")  # Print the updated set of student IDs

# Calculate remaining courses by subtracting completed courses from all courses
completed_courses = {"Biology", "Physics"}  # Set of completed courses
remaining_courses = courses - completed_courses  # Subtract completed courses from all courses
print(f"Remaining Courses: {remaining_courses}")  # Print the set of remaining courses

# Use frozen sets to create immutable sets
frozen_courses = frozenset(["Biology", "Chemistry", "Physics", "Mathematics"])  # Frozen set of courses
print(f"Frozen Courses: {frozen_courses}")  # Print the frozen set of courses

# Attempt to modify a frozen set (commented out because it will raise an error)
# frozen_courses.add("Art")  # Uncommenting this line will raise an AttributeError

# Create a frozen set of student data to make it immutable
frozen_student_data = frozenset(students)  # Frozen set of student records
print(f"Frozen Student Data: {frozen_student_data}")  # Print the frozen set of student data
