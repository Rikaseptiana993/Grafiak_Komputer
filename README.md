Game ini menampilkan transformasi geometris 2D pada objek dan player, serta memiliki fitur Game Over ketika nyawa habis. Tujuan game ini adalah memberikan pengalaman interaktif sambil memperkenalkan algoritma grafika komputer dan konsep transformasi 2D pada permainan.
Game ini bertujuan agar player dapat menangkap objek hijau yang bernilai positif dan menghindari objek merah yang bernilai negatif. Player berada di bawah layar, sedangkan objek jatuh muncul secara acak dari atas. Skor bertambah saat objek hijau tertangkap, sedangkan nyawa berkurang saat menabrak objek merah. Game berakhir ketika nyawa habis, memunculkan layar Game Over.
Setup Game dan Player
Game dibuat menggunakan Pygame, dengan layar 800x600 pixel dan 60 FPS. Player berbentuk kotak biru, bisa bergerak kiri-kanan menggunakan tombol panah, dan posisinya dibatasi agar tidak keluar layar. Player digambar menggunakan poligon, yaitu titik-titik sudut yang dihubungkan dengan garis. Perhitungan poligon: tentukan titik-titik sudut (x0,y0), (x1,y1), …, (xn,yn), lalu hubungkan tiap titik dengan algoritma garis DDA:

Hitung dx = x1 - x0, dy = y1 - y0

Tentukan step = max(|dx|, |dy|)

x_inc = dx / step, y_inc = dy / step

Iterasi dari (x0,y0), tiap langkah tambah x_inc dan y_inc sampai titik akhir, sehingga terbentuk garis lurus pixel-based.

Objek Jatuh dan Transformasi
Objek jatuh terdiri dari dua jenis: hijau dan merah. Objek hijau berbentuk lingkaran dan digambar menggunakan Midpoint Circle. Perhitungannya:

Tentukan pusat (xc,yc) dan radius r

Mulai dari titik (0,r), hitung keputusan p = 1 - r

Iterasi x dari 0 sampai x ≤ y

Jika p < 0 → y tetap, p += 2*x + 3

Jika p ≥ 0 → y -=1, p += 2*(x - y) + 5

Gambar 8 titik simetris di setiap kuadran: (xc+x, yc+y), (xc-x, yc+y), …
Objek merah berbentuk kotak menggunakan poligon seperti player. Semua objek mengalami translasi, rotasi, skala, dan refleksi sehingga tampil dinamis dan realistis.

Algoritma Grafika yang Digunakan
Beberapa algoritma grafika diterapkan secara rinci:

DDA → untuk garis lantai atau platform, menghitung dx, dy, step, x_inc, y_inc, dan menggambar pixel per langkah.

Midpoint Circle → untuk lingkaran hijau, menggunakan titik keputusan dan simetri 8 kuadran agar lingkaran digambar efisien.

Poligon → untuk player dan objek merah, titik-titik sudut dihubungkan dengan DDA dan dapat diwarnai.
Dengan algoritma ini, semua bentuk digambar akurat di layar raster.

Collision, Skor, dan Game Over
Collision detection memeriksa interaksi player dan objek: menangkap objek hijau menambah skor +10, menabrak objek merah mengurangi nyawa -1. Jika nyawa habis, muncul layar Game Over, menampilkan skor akhir. Tombol R untuk restart dan ESC untuk keluar. Mekanisme ini membuat gameplay menantang dan interaktif.

Alur Game dan Integrasi Algoritma
Alur game dimulai dari inisialisasi player dan objek, masuk ke loop game yang memperbarui posisi dan transformasi objek. Lantai digambar menggunakan DDA, player dan objek merah menggunakan poligon, dan objek hijau menggunakan Midpoint Circle. Semua elemen digabungkan dengan transformasi 2D (translasi, rotasi, skala, refleksi) untuk menghasilkan gameplay interaktif dan visual menarik.
Game ini menunjukkan penerapan nyata transformasi 2D dan algoritma grafika komputer: DDA, Midpoint Circle, dan Poligon. Mekanisme skor, nyawa, dan Game Over membuat pengalaman bermain lengkap. Refleksi menambah efek visual realistis, sementara algoritma grafika memastikan objek digambar akurat. Game ini tidak hanya interaktif tetapi juga edukatif untuk memahami grafika 2D dan transformasi geometris.
