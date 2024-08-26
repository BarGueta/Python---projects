import matplotlib.pyplot as plt
import numpy as np

# Plotting data using matplotlib:

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Regular plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('Regular Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Polar plot
plt.subplot(1, 2, 2, polar=True)
plt.plot(x, y)
plt.title('Polar Plot')

plt.show()
