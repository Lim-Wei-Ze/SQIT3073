# Sets are unordered collections of unique elements in Python.
# They are often used when you need to work with a collection of
# items where duplicates are not allowed,
# or when you need to perform set operations like union and intersection.

# Create a set
subjects = {"Math", "Science", "Art", "English"}

# Add an element to the set
subjects.add("History")

# Remove an element from the set
subjects.remove("Art")

# Check if an element is in the set
contains_science = "Science" in subjects
contains_geography = "Geography" in subjects

# Iterate through the set
print("Subjects:")
for subject in subjects:
    print(subject)

# Create another set
extra_subjects = {"Geography", "Philosophy", "Entrepreneurship"}

# Perform set operations
union_subjects_extra = subjects.union(extra_subjects)
intersection_subjects_extra = subjects.intersection(extra_subjects)
difference_subjects_extra = subjects.difference(extra_subjects)

# Print the results
print("Contains 'Science'? ", contains_science)
print("Contains 'Geography'? ", contains_geography)
print("Union of subjects and extra subjects:", union_subjects_extra)
print("Intersection of subjects and extra subjects:", intersection_subjects_extra)
print("Difference between subjects and extra subjects:", difference_subjects_extra)

# Modified by Lim Wei Ze for educational purpose
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my