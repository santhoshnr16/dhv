import os
import matplotlib.pyplot as plt
import scipy.stats as stats

# Create Graphs folder
os.makedirs("Graphs", exist_ok=True)

income = [18000, 22000, 24000, 26000, 28000,
          30000, 34000, 42000, 85000, 200000]

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(income, bins=6, edgecolor="black")

plt.title("Histogram of Monthly Income")
plt.xlabel("Monthly Income (₹)")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("Graphs/Q5_Histogram.png", dpi=300, bbox_inches="tight")
plt.show()

# Q Q Plot
plt.figure(figsize=(8, 5))
stats.probplot(income, dist="norm", plot=plt)

plt.title("Normal Q Q Plot of Monthly Income")
plt.grid(True)

plt.savefig("Graphs/Q5_QQPlot.png", dpi=300, bbox_inches="tight")
plt.show()

print("Conclusion:")
print("The monthly income data is highly positively skewed.")
print("The Q Q Plot shows clear deviation from the reference line, especially at higher incomes.")
print("Therefore, the data is not normally distributed.")