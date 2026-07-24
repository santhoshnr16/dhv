import os
import matplotlib.pyplot as plt
import scipy.stats as stats

# Create Graphs folder
os.makedirs("Graphs", exist_ok=True)

waiting_time = [12, 15, 18, 20, 22, 24, 25, 28, 30, 32]

plt.figure(figsize=(8, 5))
stats.probplot(waiting_time, dist="norm", plot=plt)

plt.title("Normal Q Q Plot of Patient Waiting Time")
plt.grid(True)

plt.savefig("Graphs/Q4_QQPlot.png", dpi=300, bbox_inches="tight")
plt.show()

print("Conclusion:")
print("The points lie close to the reference line.")
print("Therefore, the waiting times approximately follow a normal distribution.")