import pandas as pd

# Load dataset
data = pd.read_csv('googleplaystore.csv')

# -------------------------------
# Data Cleaning (IMPORTANT)
# -------------------------------

# Remove duplicates
data.drop_duplicates(inplace=True)

# Convert to numeric
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')
data['Reviews'] = pd.to_numeric(data['Reviews'], errors='coerce')

# Clean Installs column
data['Installs'] = data['Installs'].str.replace('+', '', regex=False)
data['Installs'] = data['Installs'].str.replace(',', '', regex=False)
data['Installs'] = pd.to_numeric(data['Installs'], errors='coerce')

# Clean Price column
data['Price'] = data['Price'].str.replace('$', '', regex=False)
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Drop missing values
data.dropna(inplace=True)

# -------------------------------
# EDA QUESTIONS
# -------------------------------
# 1. Display Top 5 Rows of The Dataset

print("\n1. Top 5 Rows")
print(data.head())
# 2. Check the Last 3 Rows of The Dataset

print("\n2. Last 3 Rows")
print(data.tail(3))
# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)

print("\n3. Shape of Dataset")
print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")
# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns etc
print("\n4. Dataset Info")
data.info()
# 5. Get Overall Statistics About The Dataframe

print("\n5. Overall Statistics")
print(data.describe())
# 6. Total Number of App Titles Contain Astrology

print("\n6. Apps Containing 'Astrology'")
print(data[data['App'].str.contains('Astrology', case=False)])
print("Total:", data['App'].str.contains('Astrology', case=False).sum())
# 7. Find Average App Rating

print("\n7. Average App Rating")
print(data['Rating'].mean())
# 8.  Find Total Number of Unique Category

print("\n8. Total Unique Categories")
print(data['Category'].nunique())
# 9. Which Category Getting The Highest Average Rating?

print("\n9. Category with Highest Average Rating")
print(data.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(1))
# 10. Find Total Number of App having 5 Star Rating

print("\n10. Total Apps with 5 Star Rating")
print(data[data['Rating'] == 5.0].shape[0])
# 11. Find Average Value of Reviews

print("\n11. Average Reviews")
print(data['Reviews'].mean())
# 12. Find Total Number of Free and Paid Apps

print("\n12. Free vs Paid Apps")
print(data['Type'].value_counts())
# 13.  Which App Has Maximum Reviews?

print("\n13. App with Maximum Reviews")
print(data.loc[data['Reviews'].idxmax()])
# 14. Display Top 5 Apps Having Highest Reviews

print("\n14. Top 5 Apps by Reviews")
print(data.sort_values(by='Reviews', ascending=False).head())
# 15. Find Average Rating of Free and Paid Apps

print("\n15. Average Rating of Free vs Paid Apps")
print(data.groupby('Type')['Rating'].mean())
# 16. Display Top  5 Apps Having Maximum Installs

print("\n16. Top 5 Apps with Maximum Installs")
print(data.sort_values(by='Installs', ascending=False).head())

print("\n✅ EDA Completed Successfully!")

# -------------------------------
# Save Cleaned Data
# -------------------------------
data.to_csv('cleaned_googleplaystore.csv', index=False)

print("\n✅ Analysis Completed Successfully!")