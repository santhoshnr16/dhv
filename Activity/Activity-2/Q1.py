import matplotlib.pyplot as plt
import os

# Create a folder named 'Graphs' if it doesn't already exist
os.makedirs("Graphs", exist_ok=True)

# Data
categories = [
    "Groceries",
    "Dairy",
    "Fruits",
    "Vegetables",
    "Bakery",
    "Beverages",
    "Snacks",
    "Personal Care",
    "Household Items",
    "Frozen Foods"
]

sales = [120, 95, 80, 75, 68, 90, 110, 55, 70, 60]

# Create the figure
plt.figure(figsize=(10, 6))

# Create Bar Chart
plt.bar(categories, sales, color="skyblue", edgecolor="black")

# Chart Title and Labels
plt.title("Monthly Sales Revenue by Product Category (June 2026)")
plt.xlabel("Product Category")
plt.ylabel("Sales (₹ Lakhs)")

# Rotate x-axis labels for readability
plt.xticks(rotation=30)

# Add horizontal grid lines
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Save the chart as a PNG image
plt.savefig("Graphs/Q1_Bar_Chart.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()

# Find highest and lowest selling categories
highest = max(sales)
lowest = min(sales)

highest_category = categories[sales.index(highest)]
lowest_category = categories[sales.index(lowest)]

# Print results
print("Highest Selling Category:", highest_category, "-", highest, "Lakhs")
print("Lowest Selling Category:", lowest_category, "-", lowest, "Lakhs")

# Observations
print("\nObservations:")
print("1. Groceries is the highest selling category with ₹120 Lakhs in sales.")
print("2. Personal Care is the lowest selling category with ₹55 Lakhs in sales.")