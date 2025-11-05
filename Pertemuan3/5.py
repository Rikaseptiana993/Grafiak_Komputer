# Titik awal dan akhir
x1, y1 = 0, 0
x2, y2 = 5, 3

# Hitung selisih dan jumlah langkah
dx = x2 - x1
dy = y2 - y1
n = max(abs(dx), abs(dy))  # jumlah langkah terbesar

# Hitung perubahan tiap langkah (seperti vektor)
x_inc = dx / n
y_inc = dy / n

x = x1
y = y1

print("Titik-titik koordinat garis dari (0,0) ke (5,3):")
for i in range(n + 1):
    print(f" Titik ke-{i} : ({round(x)}, {round(y)})")
    x += x_inc
    y += y_inc
