# Python Assignment 1
# Data Structures - Strings & Tuples


# ============================================================
# 1. STRING CONCATENATION
# ============================================================

string1 = "Hello "
name = input("Enter your Name: ")

string2 = string1 + name

print(string2)

string3 = ", welcome to Python programming"

string2 = string2 + string3

print(string2)


# ============================================================
# 2. STRING SLICING AND INDEXING
# ============================================================

# a. Print the first character
print("First character:", string2[0])

# b. Print the last character
print("Last character:", string2[-1])

# c. Print the first 5 characters
print("First 5 characters:", string2[:5])

# d. Print the last 11 characters
print("Last 11 characters:", string2[-11:])

# e. Print the string in reverse
print("Reverse:", string2[::-1])

# f. Print the word "Python"
print("Word Python:", string2[string2.index("Python"):string2.index("Python") + 6])


# ============================================================
# 3. STRING METHODS
# ============================================================

strM = "Python beginner tutorial"

# a. Convert the sentence to uppercase
print("Uppercase:", strM.upper())

# b. Convert the sentence to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize and return to original input form
print("Capitalize:", strM.capitalize())

# d. Count occurrences of character 't'
print("Count of 't':", strM.count("t"))

# e. Replace "Python" with "Machine Learning"
print("After replacement:", strM.replace("Python", "Machine Learning"))


# ============================================================
# 4. TUPLES
# ============================================================

# Create the first tuple
t1 = (10, 20, 30)

# Create the second tuple
t2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = t1 + t2

print("Combined tuple:", t_combine)

# b. Repeat the elements of t_combine 3 times
print("Repeated 3 times:", t_combine * 3)

# c. Access the 3rd element
print("3rd element:", t_combine[2])

# d. Access the first three elements
print("First three elements:", t_combine[:3])

# e. Access the last three elements
print("Last three elements:", t_combine[-3:])