# Create a list of transportations
transportations = ["car", "bus", "bike", "train", "plane"]

# Print the list
print("Original list:", transportations)

# Access elements by index
first_element = transportations[0]
print("The first element is:", first_element)

# Slice the list to get a subset
subset = transportations[2:4]
print("Subset of the list:", subset)

# Modify an element in the list
transportations[1] = "boat"
print("Modified list:", transportations)

# Append an element to the end of the list
transportations.append("helicopter")
print("List after appending 'helicopter':", transportations)

# Remove an element by value
transportations.remove("bike")
print("List after removing 'bike':", transportations)

# Find the index of an element
index_of_train = transportations.index("train")
print("Index of 'train':", index_of_train)

# Check if an element is in the list
contains_plane = "plane" in transportations
print("Does the list contain 'plane'?", contains_plane)

# Sort the list
transportations.sort()
print("Sorted list:", transportations)

# Reverse the list
transportations.reverse()
print("Reversed list:", transportations)

# Create a list of strings
subjects = ["Math", "Science", "Art", "English"]

print(subjects[0])

# Modified by Lim Wei Ze for educational purpose
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my