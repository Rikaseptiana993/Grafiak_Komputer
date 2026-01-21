<img width="1099" height="621" alt="Screenshot 2026-01-21 131627" src="https://github.com/user-attachments/assets/2a05202e-f534-423f-856d-46c7f6d073b7" />
Ursina Roblox-Style Obby

Kode program tersebut merupakan sebuah game 3D parkour (obby) yang dibuat menggunakan Ursina Engine dengan gaya permainan menyerupai Roblox Obby. Program diawali dengan mengimpor library Ursina, FirstPersonController, dan modul random yang digunakan untuk membangun dunia 3D, mengatur karakter pemain, serta menghasilkan variasi posisi platform. Inisialisasi `app = Ursina()` berfungsi sebagai titik awal aplikasi agar seluruh elemen game dapat dijalankan dalam satu loop utama.

Pemain direpresentasikan melalui class `RobloxPlayer` yang mewarisi `FirstPersonController`. Pada class ini, kemampuan pemain dimodifikasi agar menyerupai karakter Roblox, seperti lompatan yang lebih tinggi, kemampuan double jump, kecepatan berjalan yang stabil, serta sistem respawn otomatis ketika pemain jatuh ke bawah map. Mekanisme double jump diatur dengan pengecekan apakah pemain masih berada di udara dan belum menggunakan lompatan keduanya. Jika pemain jatuh di bawah batas tertentu, posisinya akan dikembalikan ke titik spawn atau checkpoint terakhir.

Dunia permainan dibangun dari berbagai platform kubus yang disusun secara bertahap dan relatif datar agar permainan bersifat santai. Platform tersebut terdiri dari tangga rendah, jalur penghubung, platform zig-zag, platform bergerak, platform acak, hingga platform berputar. Beberapa platform dibuat bergerak maju mundur secara perlahan, sedangkan platform lainnya berotasi secara lambat untuk menambah variasi tantangan tanpa membuat permainan terlalu sulit. Seluruh platform dilengkapi collider sehingga dapat diinjak oleh pemain.

Sistem checkpoint diterapkan untuk menyimpan progres pemain. Checkpoint berupa objek transparan yang akan aktif ketika pemain mendekatinya. Saat checkpoint tercapai, posisi spawn akan diperbarui sehingga jika pemain jatuh, ia akan muncul kembali di checkpoint terakhir yang telah dilewati. Sistem ini mencegah pemain mengulang permainan dari awal setiap kali gagal.

Selain itu, game ini juga memiliki sistem pengumpulan koin. Koin ditempatkan di beberapa lokasi strategis dan diberi animasi berputar serta naik-turun agar terlihat menarik. Ketika pemain mendekati koin, koin tersebut akan menghilang dan jumlah koin yang terkumpul akan bertambah. Informasi jumlah koin ditampilkan secara real-time melalui elemen UI di layar.

Antarmuka pengguna (UI) digunakan untuk menampilkan judul game, petunjuk kontrol, jumlah koin, status checkpoint, serta pesan kemenangan. Seluruh UI diperbarui secara dinamis selama permainan berlangsung. Ketika pemain mencapai platform finish, game akan menampilkan pesan kemenangan, menghentikan pergerakan pemain, dan memberikan opsi untuk mengulang permainan dengan menekan tombol tertentu.

Fungsi `update()` berperan sebagai pusat logika game yang dijalankan setiap frame. Fungsi ini mengatur pergerakan platform, rotasi platform, deteksi tabrakan dengan checkpoint dan koin, serta pengecekan kondisi kemenangan. Sementara itu, fungsi `input()` menangani interaksi pemain melalui keyboard, seperti keluar dari game atau mengulang permainan setelah menang.

Secara keseluruhan, kode ini membentuk sebuah game obby 3D yang terstruktur, interaktif, dan mudah dikembangkan lebih lanjut. Dengan sistem player yang responsif, checkpoint, koin, serta UI yang informatif, game ini sangat cocok digunakan sebagai media pembelajaran pengembangan game 3D menggunakan Python dan Ursina Engine.
