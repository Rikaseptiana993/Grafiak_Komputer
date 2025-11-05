# Membuat grid 10x10 berisi titik "."
grid = [["." for _ in range(10)] for _ in range(10)]

# Koordinat piksel yang diganti
x = 4
y = 6

# Ganti piksel pada posisi (x, y) menjadi "X"
grid[y][x] = "X"

# Tampilkan grid ke layar
for row in grid:
    print("".join(row))
