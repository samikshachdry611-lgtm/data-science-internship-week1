import pandas as pd

# Load the Excel file
file_path = 'global_superstore_2016.xlsx'
xls = pd.ExcelFile(file_path)

print("Available sheets in workbook:", xls.sheet_names)

# Read the Orders sheet
df = pd.read_excel(file_path, sheet_name='Orders')

# Check shape and duplicates
print(f"Initial dataset shape (Rows, Columns): {df.shape}")
print(f"Number of duplicate rows found: {df.duplicated().sum()}")

# Handle missing values in Postal Code
df['Postal Code'] = df['Postal Code'].fillna('Unknown')
print(f"Missing values in Postal Code after cleaning: {df['Postal Code'].isnull().sum()}")
print("Data cleaning completed successfully!")
# --- TASK 2 & 5: Region-wise & Category-wise Sales (Pivot Table equivalents) ---
print("\n--- REGION-WISE SALES SUMMARY ---")
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
print(region_sales.head(10))

print("\n--- CATEGORY-WISE REVENUE SUMMARY ---")
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
print(category_sales)

# --- TASK 3: Descriptive Statistics (Mean, Median, Mode for Sales) ---
print("\n--- SALES STATISTICS ---")
mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()
mode_sales = df['Sales'].mode()[0]

print(f"Mean Sales: ${mean_sales:.2f}")
print(f"Median Sales: ${median_sales:.2f}")
print(f"Mode Sales: ${mode_sales:.2f}")

# --- PROJECT SUMMARY: Total Revenue ---
total_revenue = df['Sales'].sum()
print(f"\nTotal Overall Revenue: ${total_revenue:,.2f}")
import matplotlib.pyplot as plt
import seaborn as sns

# --- TASK 5: Create a Bar Chart for Category-wise Revenue ---
plt.figure(figsize=(8, 5))
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

# Plot bar chart
sns.barplot(data=category_sales, x='Category', y='Sales', palette='Blues_d')
plt.title('Category-wise Revenue', fontsize=14, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)

# Save chart as an image
plt.savefig('category_revenue_chart.png', dpi=300, bbox_inches='tight')
print("\nChart saved successfully as 'category_revenue_chart.png' in your Downloads folder!")
plt.show()