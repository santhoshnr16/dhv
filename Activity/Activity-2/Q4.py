import matplotlib.pyplot as plt
import numpy as np
import os

# Create a folder named 'Graphs' if it doesn't already exist
os.makedirs("Graphs", exist_ok=True)

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May",
          "Jun", "Jul", "Aug", "Sep", "Oct"]

advertising = [5, 8, 10, 12, 15, 18, 20, 22, 25, 28]
sales = [42, 55, 63, 70, 82, 91, 98, 110, 120, 132]

# Create figure
plt.figure(figsize=(9, 6))

# Gradient colors
colors = np.linspace(0, 1, len(advertising))

# Scatter Plot
scatter = plt.scatter(
    advertising,
    sales,
    c=colors,
    cmap="viridis",      # Change to plasma, turbo, cool, rainbow, etc.
    s=140,
    edgecolors="black"
)

# Best-fit (trend) line
m, b = np.polyfit(advertising, sales, 1)
plt.plot(advertising,
         m * np.array(advertising) + b,
         color="red",
         linewidth=2,
         linestyle="--",
         label="Trend Line")

# Label each point
for i in range(len(months)):
    plt.text(advertising[i] + 0.3,
             sales[i] + 1,
             months[i],
             fontsize=9)

# Color bar
cbar = plt.colorbar(scatter)
cbar.set_label("Month Progression")

# Titles and Labels
plt.title("Advertising Cost vs Sales Revenue", fontsize=14, fontweight="bold")
plt.xlabel("Advertising Cost (Rs. Lakhs)", fontsize=11)
plt.ylabel("Sales Revenue (Rs. Lakhs)", fontsize=11)

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()

# Save the graph
plt.savefig("Graphs/Q4_Scatter_Plot.png", dpi=300, bbox_inches="tight")

# Display
plt.show()

# Analysis
print("Relationship: Strong Positive Correlation")

print("\nAnalysis:")
print("1. As advertising cost increases, sales revenue also increases.")
print("2. The upward trend line confirms a strong positive relationship.")
print("3. The scatter points are closely aligned with the trend line, indicating a strong correlation.")
print("4. Higher advertising expenditure is associated with higher sales revenue.")