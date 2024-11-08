import matplotlib.pyplot as plt
import numpy as np

algorithms = ['MCUVE', 'SPA', 'BS-Net-FC', 'BS-Net-C', 'Proposed']
accuracy = [0.579263 * 100, 0.54007 * 100, 0.673038 * 100, 0.725294 * 100, 0.765067 * 100]
efficiency = [0.123475, 0.012129, 0.016784, 0.00654, 0.149076]
efficiency = 1/np.log(1/np.array(efficiency))

print(efficiency)

bar_width = 0.35
index = np.arange(len(algorithms))

fig, ax1 = plt.subplots(figsize = (12,6))

bars1 = ax1.bar(index, accuracy, bar_width, label='Accuracy', color='b')

ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, efficiency, bar_width, label='Efficiency', color='g')

#ax1.set_xlabel('Algorithm')
ax1.set_ylabel('Accuracy (%)', color='b', fontsize=20)
ax2.set_ylabel('Efficiency (1/second)', color='g', fontsize=20)
ax1.set_xticks(index + bar_width / 2)
#ax1.set_xticklabels(algorithms)
ax1.set_xticklabels(['MCUVE', 'SPA', 'BS-Net-FC', 'BS-Net-C', r'$\mathbf{Proposed}$'], fontsize=24)

ax1.set_ylim(0, 100)
#ax2.set_ylim(0, 1.10)

ax1.set_yticks(np.linspace(0, 100, 5))
ax2.set_yticks([0.00, 0.25, 0.50, 0.75, 1.00])

ax1.tick_params(axis='y', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)

fig.legend(ncols=2,loc='upper left', bbox_to_anchor=(0.09,0.95), fontsize=20)
plt.tight_layout()
plt.savefig('crc.png')
#plt.show()
