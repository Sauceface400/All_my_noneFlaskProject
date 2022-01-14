import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel("cost.csv")
df.to_csv("cost.csv")
"""
x = df[{"Revenue(£)"}]
y = df[{"Cost(£)"}]

plt.plot(x, y)
plt.show()
"""