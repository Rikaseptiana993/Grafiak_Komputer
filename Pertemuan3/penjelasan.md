## 1. titik raster
<img width="486" height="460" alt="titik raster" src="https://github.com/user-attachments/assets/99b384a1-46c4-4d96-908e-b74bedb0f6b4" />
1.	Program tersebut berfungsi untuk menampilkan pola grid berukuran 10 kolom dan 5 baris menggunakan karakter titik (“.”).
2.	Dengan menggunakan dua perulangan bersarang (for), perulangan dalam mencetak titik secara horizontal sebanyak 10 kali tanpa pindah baris,
3.	sedangkan perulangan luar mengatur agar proses tersebut diulang ke bawah sebanyak 5 kali.
4.	Hasilnya adalah tampilan berupa kotak titik-titik berukuran 10×5 di layar.

## 2. titik koordinat
<img width="506" height="658" alt="titik koordinat" src="https://github.com/user-attachments/assets/c886042f-4bc6-4810-ae03-f2b83c4874ad" />
2.	Program ini digunakan untuk menghitung jarak antara dua titik dan menentukan kuadran titik pertama berdasarkan koordinat yang dimasukkan oleh pengguna. 
Setelah menerima input nilai x dan y untuk kedua titik, program menampilkan hasil berupa posisi kedua titik serta jarak di antara keduanya. 
Selain itu, program juga menganalisis tanda dari koordinat x dan y untuk menentukan apakah titik pertama berada di kuadran I, II, III, IV, di salah satu sumbu, atau tepat di titik pusat (0,0).

## 3. titik 3-2
<img width="507" height="529" alt="titik 3-2" src="https://github.com/user-attachments/assets/29f9a176-b0db-452a-bebc-c2431bd26118" />
3.	Program tersebut menampilkan pola berbentuk grid berukuran 10 kolom dan 5 baris menggunakan karakter titik (.), dengan satu titik diganti huruf x pada posisi kolom ke-3 dan baris ke-2. 
Prosesnya menggunakan dua loop for bersarang: loop luar untuk mengatur baris (y) dan loop dalam untuk kolom (x). Setiap kali kondisi x == 3 and y == 2 terpenuhi, program mencetak x, sedangkan posisi lainnya dicetak tanda titik.
Setelah satu baris selesai dicetak, perintah print() digunakan untuk berpindah ke baris berikutnya, sehingga hasilnya tampak seperti grid dengan satu tanda x di Tengah.

## 4. titik 4-6
<img width="624" height="660" alt="titik 4-6" src="https://github.com/user-attachments/assets/f8ef3c9b-7933-422a-a6ca-6f09e23f152f" />
4.	Program tersebut membuat grid berukuran 10x10 yang berisi karakter titik (.) menggunakan list dua dimensi, lalu mengganti satu titik pada koordinat tertentu (x = 4, y = 6) menjadi huruf X. 
Setelah itu, program menampilkan seluruh isi grid ke layar dengan menggunakan loop for yang mencetak setiap baris secara berurutan, sehingga hasil akhirnya terlihat seperti kotak titik dengan satu huruf X pada posisi yang ditentukan.

## 5. garis
<img width="502" height="652" alt="garis" src="https://github.com/user-attachments/assets/d1b0c396-b2b1-4522-8952-f17bca6802a4" />
5.	Program tersebut menghitung dan menampilkan koordinat titik-titik yang membentuk garis dari titik awal (0,0) ke titik akhir (5,3) menggunakan metode DDA (Digital Differential Analyzer).
Program ini terlebih dahulu menghitung selisih koordinat (dx, dy), menentukan jumlah langkah berdasarkan nilai terbesar di antara keduanya (n), lalu menghitung perubahan nilai x dan y di setiap langkah. 
Dengan melakukan iterasi sebanyak n langkah, program menampilkan koordinat hasil perhitungan secara bertahap hingga mencapai titik akhir.
