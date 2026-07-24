import matplotlib.pyplot as plt
import os

# Create a folder named 'Graphs' if it doesn't already exist
os.makedirs("Graphs", exist_ok=True)

# Salary package data (LPA)
salary = [3.2, 4.5, 5.0, 6.8, 7.2, 8.5, 4.8, 5.5, 6.0, 7.8, 9.2, 10.5]

# Create the figure
plt.figure(figsize=(8, 6))

# Create Histogram
plt.hist(salary,
         bins=5,
         color="lightgreen",
         edgecolor="black")

# Chart Title and Labels
plt.title("Distribution of Student Salary Packages")
plt.xlabel("Salary Package (LPA)")
plt.ylabel("Number of Students")

# Add grid lines
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Save the chart
plt.savefig("Graphs/Q2_Histogram.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()

# Analysis
print("Analysis:")
print("1. Salary packages range from 3.2 LPA to 10.5 LPA.")
print("2. Most students received salary packages between 4 and 8 LPA.")
print("3. The distribution has a moderate spread across the salary range.")
print("4. The highest package (10.5 LPA) appears to be a possible outlier.")