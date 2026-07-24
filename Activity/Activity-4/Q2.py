import os
import numpy as np
import matplotlib.pyplot as plt

# Create Graphs folder
os.makedirs("Graphs", exist_ok=True)

steps = [4200, 5000, 5600, 6100, 6800,
         7200, 8100, 9200, 10400, 12000]

# Sort the data
x = np.sort(steps)
y = np.arange(1, len(x) + 1) / len(x)

# Plot ECDF
plt.figure(figsize=(8, 5))
plt.step(x, y, where="post")
plt.scatter(x, y)

plt.title("ECDF of Daily Steps")
plt.xlabel("Daily Steps")
plt.ylabel("Cumulative Probability")
plt.grid(True)

plt.savefig("Graphs/Q2_ECDF.png", dpi=300, bbox_inches="tight")
plt.show()

# Proportion of participants with 8000 or fewer steps
count = np.sum(np.array(steps) <= 8000)
proportion = count / len(steps)

print("Proportion of participants who walked 8000 steps or fewer =", proportion)

print("\nInterpretation:")
print("The ECDF indicates the cumulative proportion of participants at or below any step count.")
print(f"{count} out of {len(steps)} participants walked 8000 steps or fewer.")