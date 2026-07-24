import os
import matplotlib.pyplot as plt

os.makedirs("Graphs", exist_ok=True)

response_time = [210,225,230,240,250,260,270,280,285,290,
                 300,305,310,315,320,330,340,350,360,380]

plt.figure(figsize=(8,5))
plt.hist(response_time, bins=8, edgecolor='black')

plt.title("Histogram of Website Response Time")
plt.xlabel("Response Time (ms)")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("Graphs/Q1_Histogram.png", dpi=300, bbox_inches="tight")
plt.show()