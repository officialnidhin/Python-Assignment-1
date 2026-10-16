import numpy as np
import pandas as pd

# Step 1: Create a 1D NumPy array
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

print("Week 1 Temperatures:")
print(temperatures_w1)

# Step 2: Inspect Array Properties

print("Shape:", temperatures_w1.shape)
print("Data Type:", temperatures_w1.dtype)
print("Number of Elements:", temperatures_w1.size)

# Step 3: Array Operations

# Convert Celsius to Fahrenheit
fahrenheit = (temperatures_w1 * 9/5) + 32
print("Temperatures in Fahrenheit:", fahrenheit)

# Find maximum temperature
print("Maximum Temperature:", np.max(temperatures_w1))

# Find minimum temperature
print("Minimum Temperature:", np.min(temperatures_w1))

# Find average temperature
print("Average Temperature:", np.mean(temperatures_w1))

# Step 4: Array Slicing and Indexing

# First three days
print("First three days:", temperatures_w1[:3])

# Weekend temperatures (last two days)
print("Weekend temperatures:", temperatures_w1[-2:])

# Middle three days
print("Middle three days:", temperatures_w1[2:5])

# Step 5: Create a 2D NumPy Array

temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]
])

print("Temperatures for Both Weeks:")
print(temperatures)

# Step 6: Inspect and Slice the 2D Array

# Check array properties
print("Shape:", temperatures.shape)
print("Data Type:", temperatures.dtype)
print("Total Elements:", temperatures.size)

# Extract temperatures for Week 1
print("Week 1 Temperatures:", temperatures[0])

# Extract temperatures for Week 2
print("Week 2 Temperatures:", temperatures[1])

# Extract weekend temperatures for both weeks
print("Week 1 Weekend:", temperatures[0, -2:])
print("Week 2 Weekend:", temperatures[1, -2:])

# Step 7: Create a Pandas Series

marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
)

print("Student Marks:")
print(marks)

# Step 8: Indexing and Slicing

# Access the mark of the 1st rank student using integer position
print("1st Rank Mark:", marks.iloc[0])

# Retrieve marks of the top 3 ranks using loc
print("Top 3 Ranks:")
print(marks.loc[['Rank1', 'Rank2', 'Rank3']])

# Retrieve the mark of the 3rd rank student using iloc
print("3rd Rank Mark:", marks.iloc[2])

# Find students with marks greater than 90
print("Marks Greater Than 90:")
print(marks[marks > 90])

# Step 9: Manipulating Pandas Series

# Change Rank1 mark to 100
marks.loc['Rank1'] = 100
print("Updated Marks:")
print(marks)

# Remove Rank5
marks = marks.drop('Rank5')
print("After Removing Rank5:")
print(marks)

# Calculate CGPA
cgpa = marks / 10
print("CGPA:")
print(cgpa)

# Step 10: Create a Pandas DataFrame

transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': [
        'Electronics', 'Clothing', 'Electronics', 'Furniture',
        'Clothing', 'Electronics', 'Furniture', 'Clothing',
        'Furniture', 'Electronics'
    ],
    'Region': [
        'North', 'South', 'North', 'East', 'West',
        'North', 'East', 'West', 'South', 'North'
    ],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

print("Transactions DataFrame:")
print(transactions)

# Step 11: Data Exploration

# Display first 5 rows
print("\nFirst 5 Rows:")
print(transactions.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(transactions.tail())

# Display shape
print("\nShape:")
print(transactions.shape)

# Display column names
print("\nColumn Names:")
print(transactions.columns)

# Display data types
print("\nData Types:")
print(transactions.dtypes)

# Display ProductCategory and Amount
print("\nProduct Category and Amount:")
print(transactions[['ProductCategory', 'Amount']])

# Display the last 3 columns
print("\nLast 3 Columns:")
print(transactions.iloc[:, -3:])

# Filter North region with Amount greater than 200
print("\nNorth Region Transactions Above 200:")
print(transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)])

# Count each product category
print("\nProduct Category Counts:")
print(transactions['ProductCategory'].value_counts())

# Find unique regions
print("\nUnique Regions:")
print(transactions['Region'].unique())

# Calculate average amount for each region
print("\nAverage Amount by Region:")
print(transactions.groupby('Region')['Amount'].mean())

# Step 12: Manipulating the DataFrame

# Change Amount for TransactionID 102 to 165
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165

print("\nUpdated Transaction 102:")
print(transactions[transactions['TransactionID'] == 102])

# Add Discount column (10% of Amount)
transactions['Discount'] = transactions['Amount'] * 0.10

print("\nDataFrame with Discount:")
print(transactions)

# Remove TransactionID 109
transactions = transactions[transactions['TransactionID'] != 109]

print("\nAfter Removing Transaction 109:")
print(transactions)

# Delete Discount column
transactions = transactions.drop(columns=['Discount'])

print("\nFinal DataFrame:")
print(transactions)