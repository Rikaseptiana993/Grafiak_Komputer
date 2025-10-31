# Membuat list berisi tiga pasangan titik
titik_list = [(0, 0), (50, 50), (100, 0)]

# Menampilkan semua titik dengan perulangan for
print("Daftar titik:")
for titik in titik_list:
    print(titik)

# Menyimpan satu titik dalam tuple bernama 'pusat'
pusat = (0, 0)
print("\nTitik pusat:", pusat)

# Membuat dictionary berisi atribut objek
titik = {"x": 10, "y": 20, "warna": "biru"}

# Menampilkan isi dictionary dalam format teks
print(f"Titik ({titik['x']},{titik['y']}) berwarna {titik['warna']}.")
