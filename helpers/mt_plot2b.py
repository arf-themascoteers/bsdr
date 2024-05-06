import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("combo_2b_filtered.csv")

plt.figure(figsize=(8, 6))
scatter = plt.scatter(df['band1'], df['band2'], c=df['score'], cmap='viridis', s=15)  # Decreased marker size
cb = plt.colorbar(scatter, label='Score', orientation='vertical')
#cb.set_label(label='$R^2$', rotation=0, labelpad=20, horizontalalignment='center', verticalalignment='top', fontsize=20)
# Setting label to an empty string
cb.set_label('')
cb.ax.set_title('$R^2$', loc='left', pad=10, fontsize=20)

#ax.annotate('Global maximum', (58, 59), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='red')


plt.xlabel('Band Index 1', fontsize=20)
plt.ylabel('Band Index 2', fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("fig1.png")