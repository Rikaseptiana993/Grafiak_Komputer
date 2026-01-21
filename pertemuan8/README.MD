
3D

Kode program tersebut merupakan sebuah game mini TPS (Third Person Shooter) yang dibuat menggunakan Pygame sebagai pengelola window dan input, serta OpenGL untuk rendering grafis 3D. Pada bagian awal, program mengimpor modul yang diperlukan seperti OpenGL untuk menggambar objek 3D, matematika untuk perhitungan jarak dan sudut, serta random untuk menentukan posisi musuh secara acak. Setelah itu, struktur dasar kubus didefinisikan melalui kumpulan titik (vertices) dan sisi (surfaces) yang digunakan sebagai **blok utama** untuk membentuk seluruh objek 3D di dalam game.

Kubus menjadi elemen dasar untuk hampir semua objek, termasuk lantai, pemain, senjata, musuh, dan peluru. Fungsi `cube()` bertugas menggambar kubus dengan warna tertentu menggunakan OpenGL. Sementara itu, fungsi `floor()` membuat lantai besar berwarna abu-abu yang berfungsi sebagai arena permainan. Dengan pendekatan ini, game menggunakan bentuk geometri sederhana namun efektif untuk membangun dunia 3D.

Model senjata dibuat pada fungsi `detailed_gun()` dengan menggabungkan beberapa kubus yang diskalakan, diputar, dan diposisikan sedemikian rupa sehingga menyerupai senjata 3D. Senjata ini kemudian dipasang pada model pemain melalui fungsi `player_model()`. Model pemain sendiri terdiri dari tubuh, kepala, dan tangan, yang semuanya dibentuk dari kubus dan dirender dalam perspektif orang ketiga (third person).

Musuh direpresentasikan melalui class `Enemy` yang memiliki atribut kecepatan dan posisi. Setiap musuh akan bergerak mendekati posisi pemain dengan menghitung arah menggunakan jarak Euclidean. Jika musuh terlalu dekat dengan pemain, maka darah (HP) pemain akan berkurang. Sistem ini menciptakan mekanisme **kejar-kejaran** khas game shooter, di mana pemain harus menembak musuh sebelum musuh mencapai dirinya.

Efek ledakan diimplementasikan menggunakan class `Explosion`, yang bekerja dengan konsep partikel sederhana. Ketika musuh terkena peluru, beberapa partikel akan muncul dan menyebar ke berbagai arah dengan kecepatan dan umur tertentu. Partikel ini diperbarui setiap frame hingga habis, sehingga menciptakan efek visual ledakan yang dinamis meskipun menggunakan objek kubus sederhana.

Pada bagian utama program (`main()`), window game dibuat dengan mode OpenGL dan pengaturan kamera perspektif 3D. Kamera ditempatkan di belakang pemain untuk menciptakan sudut pandang third person. Mouse digunakan untuk mengatur rotasi arah pandang (yaw), sedangkan keyboard digunakan untuk menggerakkan pemain. Saat klik mouse kiri, peluru akan ditembakkan ke arah pandangan pemain.

Game menggunakan sistem wave atau gelombang musuh. Setiap wave akan memunculkan sejumlah musuh yang semakin banyak dan semakin cepat seiring bertambahnya level. Pemain mendapatkan skor setiap kali berhasil mengalahkan musuh. Jika darah pemain habis, status game akan berubah menjadi game over, namun pemain dapat mengulang permainan dengan menekan tombol tertentu.

Secara keseluruhan, kode ini menggambarkan implementasi dasar game TPS 3D menggunakan Python tanpa engine game modern. Program ini mencakup konsep penting dalam pengembangan game, seperti rendering 3D, pergerakan kamera, collision sederhana, sistem musuh, sistem skor, efek visual ledakan, serta loop game real-time. Kode ini sangat cocok digunakan sebagai media pembelajaran dasar pembuatan game 3D dan logika game shooter menggunakan Pygame dan OpenGL.

  
