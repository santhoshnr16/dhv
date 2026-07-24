import os
import numpy as np
import matplotlib.pyplot as plt

# Create Graphs folder
os.makedirs("Graphs", exist_ok=True)

marks = [45, 52, 58, 60, 65, 68, 72, 75, 80, 90]

# Sort the data
x = np.sort(marks)
y = np.arange(1, len(x) + 1) / len(x)

# Plot ECDF
plt.figure(figsize=(8, 5))
plt.step(x, y, where="post")
plt.scatter(x, y)

plt.title("Empirical Cumulative Distribution Function (ECDF)")
plt.xlabel("Marks")
plt.ylabel("Cumulative Probability")
plt.grid(True)

plt.savefig("Graphs/Q1_ECDF.png", dpi=300, bbox_inches="tight")
plt.show()

print("Student Marks and Cumulative Probability")
for mark, prob in zip(x, y):
    print(f"{mark} : {prob:.2f}")

print("\nInterpretation:")
print("The ECDF shows the cumulative proportion of students scoring at or below each mark.")