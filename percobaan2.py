import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5,5))

# Plot data dengan label
plt.plot(xpoints, ypoints, color='red', marker='o', linestyle='-', label='Data Points')

# Menambahkan label pada sumbu X dan Y
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Menambahkan judul plot
plt.title('Grafik Data')

# Menambahkan legenda
plt.legend()

# Mengatur batas sumbu X dan Y
plt.xlim([0, 15])
plt.ylim([0, 15])

# Menampilkan plot
plt.show()
