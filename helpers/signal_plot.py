import pandas as pd
import matplotlib.pyplot as plt

lucas = pd.read_csv("../data/lucas.csv")
data = lucas.iloc[120,1::10].to_numpy()
x = list(range(data.shape[0]))
#plt.figure(figsize=(8, 3))
plt.scatter(x,data, marker=".", s=10)
plt.xticks([])
plt.yticks([])
plt.xlabel("Band Index", fontsize=18)
plt.ylabel("Reflectance", fontsize=18)
plt.show()

# plt.plot(x,data)
# plt.xticks([])
# plt.yticks([])
# plt.gca().spines['top'].set_visible(False)
# plt.gca().spines['right'].set_visible(False)
# plt.gca().spines['bottom'].set_visible(False)
# plt.gca().spines['left'].set_visible(False)

plt.show()
