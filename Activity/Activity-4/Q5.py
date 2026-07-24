import os
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

# Create Graphs folder
os.makedirs("Graphs", exist_ok=True)

income = [18000, 22000, 24000, 26000, 28000,
          30000, 34000, 42000, 85000, 200000]

data = pd.Series(income)

# Histogram
plt.figure(figsize=(8,5))
plt.hist(income, bins=6, edgecolor="black")

plt.title("Histogram of Monthly Income")
plt.xlabel("Monthly Income (₹)")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("Graphs/Q5_Histogram.png", dpi=300, bbox_inches="tight")
plt.show()

# Normal Q Q Plot
plt.figure(figsize=(8,5))
stats.probplot(income, dist="norm", plot=plt)

plt.title("Normal Q Q Plot of Monthly Income")
plt.grid(True)

plt.savefig("Graphs/Q5_QQPlot.png", dpi=300, bbox_inches="tight")
plt.show()

# Determine Skewness
skew = data.skew()

print("Skewness =", round(skew, 2))

if skew > 0:
    print("The income data is highly positively skewed.")
elif skew < 0:
    print("The income data is negatively skewed.")
else:
    print("The income data is symmetric.")

print("\nConclusion:")
print("1. The histogram shows that most customers have low to moderate incomes, while one customer has an exceptionally high income.")
print("2. The Q Q Plot shows noticeable deviation from the reference line, especially in the upper tail.")
print("3. Therefore, the monthly income data is not normally distributed and is highly positively skewed.")
print("4. The Q Q Plot supports this conclusion because the data points do not closely follow the straight reference line.")