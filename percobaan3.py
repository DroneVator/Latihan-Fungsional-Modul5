import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 9, 4, 8])  # Data untuk garis ketiga

# Membuat plot untuk garis y1, y2, dan y3 dengan warna dan corak/bentuk yang berbeda
plt.plot(y1, label='Garis 1', color='blue', linestyle='-', marker='o')
plt.plot(y2, label='Garis 2', color='green', linestyle='--', marker='s')
plt.plot(y3, label='Garis 3', color='red', linestyle=':', marker='^')

# Menambahkan judul dan label sumbu
plt.title('Plot Tiga Garis')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Menambahkan keterangan (legend)
plt.legend()
plt.show()
