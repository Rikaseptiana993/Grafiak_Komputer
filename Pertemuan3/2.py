import math 
x1 = float(input("Masukkan koordinat x1: "))
y1 = float(input("Masukkan koordinat y1: "))
x2 = float(input("Masukkan koordinat x2: "))
y2 = float(input("Masukkan koordinat y2: "))

print ("\n ==== HASIL ==== \n")

print(f"Titik pertama ({x1}, {y1})")
print(f"Titik pertama ({x2}, {y2})")

jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Tentukan kuadran titik pertama
if x1 > 0 and y1 > 0:
    kuadran = "Kuadran I"
elif x1 < 0 and y1 > 0:
    kuadran = "Kuadran II"
elif x1 < 0 and y1 < 0:
    kuadran = "Kuadran III"
elif x1 > 0 and y1 < 0:
    kuadran = "Kuadran IV"
elif x1 == 0 and y1 == 0:
    kuadran = "Titik pusat (0,0)"
elif x1 == 0:
    kuadran = "Berada di sumbu Y"
elif y1 == 0:
    kuadran = "Berada di sumbu X"
else:
    kuadran = "Tidak diketahui"

# Tampilkan hasil
print(f"\nJarak antara dua titik: {jarak:.2f}")
print(f"Titik pertama berada di: {kuadran}")


