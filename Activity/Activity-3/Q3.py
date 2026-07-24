import os
import matplotlib.pyplot as plt
import pandas as pd

# Create Graphs folder
os.makedirs("Graphs", exist_ok=True)

purchase_amount = [250, 300, 320, 350, 380,
                   450, 520, 650, 1800, 5200]

data = pd.Series(purchase_amount)

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(purchase_amount, bins=6, edgecolor="black")

plt.title("Histogram of Customer Purchase Amount")
plt.xlabel("Purchase Amount (₹)")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("Graphs/Q3_Histogram.png", dpi=300, bbox_inches="tight")
plt.show()

# Density Plot
plt.figure(figsize=(8, 5))
data.plot(kind="density")

plt.title("Density Plot of Customer Purchase Amount")
plt.xlabel("Purchase Amount (₹)")
plt.grid(True)

plt.savefig("Graphs/Q3_DensityPlot.png", dpi=300, bbox_inches="tight")
plt.show()

# Skewness
skew = data.skew()
print("Skewness =", round(skew, 2))

if skew > 0:
    print("The distribution is Positively Skewed.")
elif skew < 0:
    print("The distribution is Negatively Skewed.")
else:
    print("The distribution is Symmetric.")

print("\nJustification:")
print("Most customers purchased low priced items, while a few customers made very high value purchases.")
print("Therefore, the distribution has a long right tail and is positively skewed.")