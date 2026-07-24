import matplotlib.pyplot as plt
import os

# Create a folder named 'Graphs' if it doesn't already exist
os.makedirs("Graphs", exist_ok=True)

# Data
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

energy = [420, 450, 490, 530, 560, 600, 580, 590, 610, 630, 590, 540]

# Create figure
plt.figure(figsize=(10, 6))

# Plot the line
plt.plot(
    months,
    energy,
    color="royalblue",
    linewidth=3,
    marker="o",
    markersize=8,
    markerfacecolor="gold",
    markeredgecolor="black",
    label="Energy Generated"
)

# Fill the area below the line
plt.fill_between(months, energy, color="skyblue", alpha=0.3)

# Find highest and lowest values
highest = max(energy)
lowest = min(energy)

highest_month = months[energy.index(highest)]
lowest_month = months[energy.index(lowest)]

# Highlight highest point
plt.scatter(highest_month, highest, color="green", s=180,
            edgecolors="black", zorder=5, label="Highest")

# Highlight lowest point
plt.scatter(lowest_month, lowest, color="red", s=180,
            edgecolors="black", zorder=5, label="Lowest")

# Annotate highest point
plt.annotate(
    f"Highest\n{highest} MWh",
    xy=(highest_month, highest),
    xytext=(highest_month, highest + 25),
    arrowprops=dict(arrowstyle="->", color="green"),
    fontsize=10,
    color="green",
    ha="center"
)

# Annotate lowest point
plt.annotate(
    f"Lowest\n{lowest} MWh",
    xy=(lowest_month, lowest),
    xytext=(lowest_month, lowest - 50),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10,
    color="red",
    ha="center"
)

# Title and Labels
plt.title("Monthly Solar Energy Generation (2025)", fontsize=14, fontweight="bold")
plt.xlabel("Month", fontsize=11)
plt.ylabel("Energy Generated (MWh)", fontsize=11)

# Grid
plt.grid(True, linestyle="--", alpha=0.5)

# Legend
plt.legend()

# Save graph
plt.savefig("Graphs/Q5_Line_Chart.png", dpi=300, bbox_inches="tight")

# Display graph
plt.show()

# Print Results
print("Highest Energy Production:", highest_month, "-", highest, "MWh")
print("Lowest Energy Production:", lowest_month, "-", lowest, "MWh")

print("\nAnalysis:")
print("1. Energy generation steadily increases from January to June.")
print("2. There is a slight decrease in July before rising again.")
print("3. The highest energy generation occurs in October (630 MWh).")
print("4. The lowest energy generation occurs in January (420 MWh).")
print("5. The trend suggests seasonal variations, with production peaking during late summer and early autumn before declining towards December.")