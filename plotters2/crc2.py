import matplotlib.pyplot as plt
import numpy as np

algorithms = ['MCUVE', 'SPA', 'BS-Net-FC', 'BS-Net-C', 'Proposed']
accuracy = [0.579263 * 100, 0.54007 * 100, 0.673038 * 100, 0.725294 * 100, 0.815067 * 100]
efficiency = [0.113475, 0.012129, 0.016784, 0.00654, 0.099076]
efficiency = 1/np.log(1/np.array(efficiency))

print(efficiency)

bar_width = 0.35
index = np.arange(len(algorithms))

fig, ax1 = plt.subplots(figsize = (12,12))

bars1 = ax1.bar(index, accuracy, bar_width, label='Accuracy', color='#00344a')

ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, efficiency, bar_width, label='Efficiency', color='#97bf0d')

#ax1.set_xlabel('Algorithm')
ax1.set_ylabel('Accuracy (%)', color='#00344a', fontsize=34)
ax2.set_ylabel('Efficiency (1/second)', color='#97bf0d', fontsize=34, labelpad=20)
ax1.set_xticks(index + bar_width / 2)
#ax1.set_xticklabels(algorithms)
ax1.set_xticklabels(['MCUVE', 'SPA', 'BS-Net-FC', 'BS-Net-C', r'$\mathbf{Proposed}$'], fontsize=20)

ax1.set_ylim(0, 100)
ax2.set_ylim(0, 0.8)

ax1.set_yticks(np.linspace(0, 100, 5))
ax2.set_yticks([0.00, 0.25, 0.50, 0.75, 1.00])

ax1.tick_params(axis='y', labelsize=28, labelcolor="#00344a")
ax2.tick_params(axis='y', labelsize=28, labelcolor="#97bf0d")

# ax1.set_yticks([])
# ax2.set_yticks([])

fig.legend(ncols=2,loc='upper left', bbox_to_anchor=(0.12,0.95), fontsize=34)
plt.tight_layout()
plt.savefig('crc2.png', transparent=True)
plt.show()
