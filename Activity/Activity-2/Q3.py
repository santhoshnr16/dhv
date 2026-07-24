import matplotlib.pyplot as plt
import os

# Create a folder named 'Graphs' if it doesn't already exist
os.makedirs("Graphs", exist_ok=True)

# Data
channels = [
    "Social Media",
    "Television",
    "Print Media",
    "Radio",
    "Email Marketing",
    "Influencer Marketing",
    "SEO",
    "Events"
]

budget = [28, 22, 10, 8, 12, 9, 6, 5]

# Create the figure
plt.figure(figsize=(8, 8))

# Create Pie Chart
plt.pie(
    budget,
    labels=channels,
    autopct="%1.1f%%",
    startangle=90
)

# Chart Title
plt.title("Marketing Budget Allocation")

# Save the chart
plt.savefig("Graphs/Q3_Pie_Chart.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()

# Find highest investment
highest = max(budget)
highest_channel = channels[budget.index(highest)]

# Print analysis
print("Highest Investment Channel:", highest_channel, "-", highest, "%")

print("\nAnalysis:")
print("1. Social Media receives the highest budget allocation at 28%.")
print("2. Television is the second-highest investment with 22%.")
print("3. Social Media and Television together account for 50% of the total marketing budget.")
print("4. SEO and Events receive the smallest portions of the budget.")