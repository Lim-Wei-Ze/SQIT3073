# Create a tuple
subjects = ("Math", "Science", "Art", "English")

( "a" , 1 , 2.3 , "b" )

# Access elements by index
first_subject = subjects[0]
second_subject = subjects[1]

# Iterate through the tuple
print("Subjects:")
for subject in subjects:
    print(subject)

# Check if an element is in the tuple
contains_art = "Art" in subjects

# Find the length of the tuple
num_subjects = len(subjects)

# Concatenate two tuples
more_subjects = ("History", "Geography")
all_subjects = subjects + more_subjects

# Nested tuple
nested_tuple = ("Core", ("Elective", "Optional"))

# Print the results
print("First subject:", first_subject)
print("Second subject:", second_subject)
print("Does it contain 'Art'? ", contains_art)
print("Number of subjects:", num_subjects)
print("All subjects:", all_subjects)
print("Nested tuple:", nested_tuple)

# Modified by Lim Wei Ze for educational purpose
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
