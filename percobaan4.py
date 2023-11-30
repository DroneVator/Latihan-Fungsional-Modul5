import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

plt.scatter(x, y)
plt.show()

#SETEKAG DI KREASIKAN
# import matplotlib.pyplot as plt
# import numpy as np

# # Data awal
# x = [1, 2, 3, 4, 5]
# y = [3, 7, 2, 8, 5]

# # Scatter plot untuk data awal
# plt.scatter(x, y, label='Data Awal', color='blue', marker='o')

# # Menambahkan variasi baru dengan data kedua
# x2 = np.arange(1, 6, 0.5)
# y2 = np.sin(x2) + 5  # Contoh variasi menggunakan fungsi sin

# # Scatter plot untuk data kedua
# plt.scatter(x2, y2, label='Data Baru', color='red', marker='^')

# # Menambahkan judul dan label sumbu
# plt.title('Scatter Plot dengan Variasi')
# plt.xlabel('Sumbu X')
# plt.ylabel('Sumbu Y')

# # Menambahkan legenda
# plt.legend()

# # Menampilkan plot
# plt.show()
