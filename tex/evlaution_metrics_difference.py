import matplotlib.pyplot as plt
import numpy as np

# Data
metrics = ['Perplexity', 'Distinct-1', 'Distinct-2', 'Success Rate']
your_work = [8.84, 0.26, 0.58, 0.9179]
madotto2021 = [9.5, 0, 0, 0]  
chung2023 = [36.63, 0, 0, 0.7848]  
kasahara2022 = [0, 0.231, 0.595, 0]  
hu2024 = [0, 0, 0, 0.851]  

# Combine data for plotting
data = np.array([your_work, madotto2021, chung2023, kasahara2022, hu2024])

x = np.arange(len(metrics))  # Label locations
width = 0.15  # Width of the bars

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - 2*width, your_work, width, label='Offered System')
bars2 = ax.bar(x - width, madotto2021, width, label='Madotto et al. (2021)')
bars3 = ax.bar(x, chung2023, width, label='Chung et al. (2023)')
bars4 = ax.bar(x + width, kasahara2022, width, label='Kasahara et al. (2022)')
bars5 = ax.bar(x + 2*width, hu2024, width, label='Hu et al. (2024)')

# Set log scale for y-axis
ax.set_yscale('log')

# Add labels, title, and legend
ax.set_xlabel('Metrics')
ax.set_ylabel('Values')
ax.set_title('Compare values of different metrics')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
