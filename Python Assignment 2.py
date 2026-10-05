# Python Assignment 2
# Part 1 - List Creation, Modification and Access

# 1. List Creation

# a. Create age_list with five integer elements
age_list = [24, 25, 26, 27, 28]

# b. Create name_list with five string elements
name_list = ["Arun", "Rahul", "Nikhil", "Akhil", "Vijay"]


# 2. List Operations / Modifications

# a. Append "Yazhini" to name_list
name_list.append("Yazhini")

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)

# c. Remove "Yazhini" from name_list
name_list.remove("Yazhini")

# d. Pop the last element from age_list
age_list.pop()

# e. Extend age_list with additional ages
age_list.extend([29, 30, 26])

# f. Sort age_list in descending order
age_list.sort(reverse=True)

# g. Find maximum age, minimum age and sum of all ages
maximum_age = max(age_list)
minimum_age = min(age_list)
total_age = sum(age_list)


# Print the results

print("Age List:", age_list)
print("Name List:", name_list)
print("Maximum Age:", maximum_age)
print("Minimum Age:", minimum_age)
print("Sum of All Ages:", total_age)


# 3. Accessing List Elements

# a. Print the first element of name_list
print("First element:", name_list[0])

# b. Print the last element of name_list
print("Last element:", name_list[-1])

# c. Print elements from index 2 to index 4
print("Elements from index 2 to 4:", name_list[2:5])

# d. Print name_list in reverse order
print("Reverse order:", name_list[::-1])

# ==========================================
# Part 2 - Dictionary Creation, Modification and Access
# ==========================================

# a. Create a dictionary with five students and their marks
student_marks = {
    "Arun": 75,
    "Rahul": 88,
    "Nikhil": 65,
    "Akhil": 92,
    "Vijay": 78
}

# b. Access and print the mark of a specific student
print("Rahul's mark:", student_marks["Rahul"])

# c. Add a new student Janani with a mark of 80
student_marks["Janani"] = 80

# d. Update the mark of an older student to 82
student_marks["Nikhil"] = 82

# e. Print all keys, values and key-value pairs

print("All student names:", student_marks.keys())

print("All marks:", student_marks.values())

print("All student marks:", student_marks.items())

# ==========================================
# Part 3 - Sets
# ==========================================

# a. Create a set with the given values
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My Set:", my_set)

# Explanation:
# A set does not allow duplicate values.
# Therefore, duplicate 'a' and 'i' values are automatically removed.


# b. Attempt to change the value at index 4
try:
    my_set[4] = 's'
except TypeError as e:
    print("Error while changing set value:", e)
    print("Explanation: Sets are unordered and do not support indexing.")


# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}


# d. Compute and print union and intersection
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

print("Union of set1 and set2:", union_set)
print("Intersection of set1 and set2:", intersection_set)

# ==========================================
# Part 4 - Conditional Statements
# Performance Category Program
# ==========================================

# Get score from the user
score = float(input("Enter your score (0 to 10): "))

# Check the performance category
if score > 7 and score <= 10:
    print("Above Average: Excellent performance! Keep up the great work.")

elif score >= 4 and score <= 7:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

elif score >= 0 and score < 4:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")

else:
    print("Invalid score. Please enter a score between 0 and 10.")