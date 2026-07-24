import os
import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("Graphs", exist_ok=True)

response_time = [210,225,230,240,250,260,270,280,285,290,
                 300,305,310,315,320,330,340,350,360,380]

data = pd.Series(response_time)

plt.figure(figsize=(8,5))
data.plot(kind="density")

plt.title("Density Plot of Website Response Time")
plt.xlabel("Response Time (ms)")
plt.grid(True)

plt.savefig("Graphs/Q2_DensityPlot.png", dpi=300, bbox_inches="tight")
plt.show()