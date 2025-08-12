# Week Two Assignment - Python Lists
# Author: Mwanaisha Salim
# Purpose: Practice Python list operations

# Step 1: Create an empty list
my_list = []

# Step 2: Append elements to the list
# I'm adding them one by one using append()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
# Lists use zero-based indexing, so index 1 is the 2nd position
my_list.insert(1, 15)

# Step 4: Extend the list with another list [50, 60, 70]
extra_items = [50, 60, 70]
my_list.extend(extra_items)

# Step 5: Remove the last element
# pop() with no index removes the last item
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find the index of value 30
index_of_30 = my_list.index(30)

# Output results in a neat way
print("Final list after all operations:", my_list)
print("Index of 30 in the list:", index_of_30)
