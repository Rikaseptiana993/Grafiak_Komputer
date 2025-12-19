import pygame
import math
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Game 2D - Karakter Lucu")

# Warna
PUTIH = (255, 255, 255)
HITAM = (0, 0, 0)
BIRU = (100, 150, 255)
HIJAU = (100, 200, 100)
COKLAT = (139, 69, 19)
KUNING = (255, 255, 100)
MERAH = (255, 100, 100)
PINK = (255, 182, 193)
ORANGE = (255, 165, 0)

# Clock
clock = pygame.time.Clock()

# Posisi dan properti karakter pemain
pos_x = 400
pos_y = 300
kecepatan = 5
rotasi = 0
skala = 1.0
flip_horizontal = False
pedang_aktif = False

# Animasi karakter
frame_animasi = 0
arah_lompat = 1  # Untuk efek bouncing
offset_lompat = 0

# Posisi dan properti musuh
musuh_x = 600
musuh_y = 300
musuh_rotasi = 0
musuh_skala = 1.0
musuh_flip = True
musuh_pedang_aktif = False
musuh_arah_x = -1
musuh_arah_y = 0.5

# Score dan waktu
score = 0
combo = 0
waktu_combo = 0
hit_cooldown = 0

# Partikel untuk efek
partikel = []

def gambar_latar():
    """Menggambar latar belakang yang menarik"""
    # Langit gradasi
    for i in range(TINGGI // 2):
        warna = (100 + i // 3, 150 + i // 3, 255)
        pygame.draw.line(layar, warna, (0, i), (LEBAR, i))
    
    # Rumput
    pygame.draw.rect(layar, HIJAU, (0, TINGGI // 2, LEBAR, TINGGI // 2))
    
    # Matahari
    pygame.draw.circle(layar, KUNING, (700, 100), 40)
    pygame.draw.circle(layar, (255, 255, 150), (700, 100), 35)
    
    # Awan
    pygame.draw.ellipse(layar, PUTIH, (100, 80, 80, 40))
    pygame.draw.ellipse(layar, PUTIH, (130, 70, 70, 40))
    pygame.draw.ellipse(layar, PUTIH, (160, 80, 80, 40))
    
    pygame.draw.ellipse(layar, PUTIH, (500, 120, 90, 45))
    pygame.draw.ellipse(layar, PUTIH, (540, 110, 80, 45))
    
    # Pohon
    pygame.draw.rect(layar, COKLAT, (50, 350, 30, 80))
    pygame.draw.circle(layar, (50, 150, 50), (65, 340), 40)
    pygame.draw.circle(layar, (50, 150, 50), (45, 320), 35)
    pygame.draw.circle(layar, (50, 150, 50), (85, 320), 35)

def gambar_karakter_lucu(x, y, rotasi, skala, flip, frame, offset_y=0, dengan_pedang=False):
    """Menggambar karakter garang dengan animasi"""
    ukuran = int(60 * skala)
    karakter_surface = pygame.Surface((ukuran * 4, ukuran * 4), pygame.SRCALPHA)
    
    tengah_x = ukuran * 2
    tengah_y = ukuran * 2 + offset_y
    
    # Bayangan karakter (lebih gelap dan tajam)
    bayangan_y = tengah_y + int(45 * skala)
    pygame.draw.ellipse(karakter_surface, (0, 0, 0, 100), 
                       (tengah_x - int(30 * skala), bayangan_y - int(5 * skala),
                        int(60 * skala), int(15 * skala)))
    
    # Kaki berotot dan kuat
    kaki_kiri_x = tengah_x - int(12 * skala)
    kaki_kanan_x = tengah_x + int(4 * skala)
    kaki_y = tengah_y + int(25 * skala)
    
    # Animasi kaki bergerak agresif
    offset_kaki = math.sin(frame * 0.4) * 5 * skala
    
    # Kaki kiri (berotot)
    pygame.draw.rect(karakter_surface, (80, 80, 80),
                    (kaki_kiri_x, kaki_y + offset_kaki, 
                     int(12 * skala), int(20 * skala)))
    pygame.draw.rect(karakter_surface, (60, 60, 60),
                    (kaki_kiri_x, kaki_y + offset_kaki + int(15 * skala), 
                     int(14 * skala), int(8 * skala)))
    
    # Kaki kanan (berotot)
    pygame.draw.rect(karakter_surface, (80, 80, 80),
                    (kaki_kanan_x, kaki_y - offset_kaki, 
                     int(12 * skala), int(20 * skala)))
    pygame.draw.rect(karakter_surface, (60, 60, 60),
                    (kaki_kanan_x, kaki_y - offset_kaki + int(15 * skala), 
                     int(14 * skala), int(8 * skala)))
    
    # Badan kekar dan berotot (dengan armor)
    # Base body
    pygame.draw.rect(karakter_surface, (40, 40, 40),
                    (tengah_x - int(20 * skala), tengah_y - int(5 * skala),
                     int(40 * skala), int(30 * skala)))
    
    # Armor chest plate
    for i in range(3):
        pygame.draw.rect(karakter_surface, (100 - i*10, 0, 0),
                        (tengah_x - int((18 - i*2) * skala), tengah_y - int(3 * skala),
                         int((36 - i*4) * skala), int(26 * skala)))
    
    # Shoulder pads (bahu lebar)
    pygame.draw.polygon(karakter_surface, (60, 0, 0), [
        (tengah_x - int(22 * skala), tengah_y - int(8 * skala)),
        (tengah_x - int(32 * skala), tengah_y - int(12 * skala)),
        (tengah_x - int(28 * skala), tengah_y + int(5 * skala))
    ])
    pygame.draw.polygon(karakter_surface, (60, 0, 0), [
        (tengah_x + int(22 * skala), tengah_y - int(8 * skala)),
        (tengah_x + int(32 * skala), tengah_y - int(12 * skala)),
        (tengah_x + int(28 * skala), tengah_y + int(5 * skala))
    ])
    
    # Spike di shoulder
    for spike_x in [-27, 27]:
        pygame.draw.polygon(karakter_surface, (120, 120, 120), [
            (tengah_x + int(spike_x * skala), tengah_y - int(12 * skala)),
            (tengah_x + int((spike_x - 3) * skala), tengah_y - int(8 * skala)),
            (tengah_x + int((spike_x + 3) * skala), tengah_y - int(8 * skala))
        ])
    
    # Tangan kiri berotot dengan animasi
    tangan_kiri_y = tengah_y + int(5 * skala) + math.sin(frame * 0.3) * 3
    # Lengan atas
    pygame.draw.rect(karakter_surface, (80, 80, 80),
                    (tengah_x - int(38 * skala), tangan_kiri_y - int(8 * skala),
                     int(14 * skala), int(22 * skala)))
    # Lengan bawah
    pygame.draw.rect(karakter_surface, (70, 70, 70),
                    (tengah_x - int(40 * skala), tangan_kiri_y + int(12 * skala),
                     int(14 * skala), int(18 * skala)))
    # Sarung tangan dengan cakar
    pygame.draw.polygon(karakter_surface, (50, 50, 50), [
        (tengah_x - int(40 * skala), tangan_kiri_y + int(30 * skala)),
        (tengah_x - int(26 * skala), tangan_kiri_y + int(30 * skala)),
        (tengah_x - int(33 * skala), tangan_kiri_y + int(38 * skala))
    ])
    
    # Tangan kanan (yang memegang pedang)
    tangan_kanan_y = tengah_y + int(5 * skala) - math.sin(frame * 0.3) * 3
    if dengan_pedang:
        tangan_kanan_y = tengah_y - int(5 * skala)  # Angkat tinggi saat menyerang
    
    # Lengan atas
    pygame.draw.rect(karakter_surface, (80, 80, 80),
                    (tengah_x + int(24 * skala), tangan_kanan_y - int(8 * skala),
                     int(14 * skala), int(22 * skala)))
    # Lengan bawah
    pygame.draw.rect(karakter_surface, (70, 70, 70),
                    (tengah_x + int(26 * skala), tangan_kanan_y + int(12 * skala),
                     int(14 * skala), int(18 * skala)))
    
    # Pedang GARANG dengan efek api
    if dengan_pedang:
        # Gagang pedang hitam
        pygame.draw.rect(karakter_surface, (20, 20, 20),
                        (tengah_x + int(40 * skala), tangan_kanan_y + int(15 * skala),
                         int(18 * skala), int(12 * skala)))
        pygame.draw.circle(karakter_surface, (150, 0, 0),
                          (int(tengah_x + 49 * skala), int(tangan_kanan_y + 21 * skala)), int(7 * skala))
        
        # Bilah pedang merah menyala
        for i in range(5, 0, -1):
            intensity = i * 30
            pygame.draw.polygon(karakter_surface, (intensity + 100, intensity // 2, 0), [
                (tengah_x + int((58 - i) * skala), tangan_kanan_y + int(10 * skala)),
                (tengah_x + int((95 + i) * skala), tangan_kanan_y + int(21 * skala)),
                (tengah_x + int((58 - i) * skala), tangan_kanan_y + int(32 * skala))
            ])
        
        # Efek api di bilah pedang (animasi)
        if frame % 4 < 2:
            for flame_offset in range(3):
                flame_x = tengah_x + int((65 + flame_offset * 10) * skala)
                flame_y = tangan_kanan_y + int((21 + random.randint(-3, 3)) * skala)
                pygame.draw.circle(karakter_surface, (255, 150, 0), 
                                 (int(flame_x), int(flame_y)), int(3 * skala))
        
        # Ujung pedang tajam
        pygame.draw.polygon(karakter_surface, (255, 255, 200), [
            (tengah_x + int(92 * skala), tangan_kanan_y + int(19 * skala)),
            (tengah_x + int(100 * skala), tangan_kanan_y + int(21 * skala)),
            (tengah_x + int(92 * skala), tangan_kanan_y + int(23 * skala))
        ])
    
    # Sarung tangan
    pygame.draw.polygon(karakter_surface, (50, 50, 50), [
        (tengah_x + int(26 * skala), tangan_kanan_y + int(30 * skala)),
        (tengah_x + int(40 * skala), tangan_kanan_y + int(30 * skala)),
        (tengah_x + int(33 * skala), tangan_kanan_y + int(38 * skala))
    ])
    
    # Kepala dengan helm
    # Base kepala
    pygame.draw.circle(karakter_surface, (70, 70, 70),
                      (int(tengah_x), int(tengah_y - 25 * skala)), int(22 * skala))
    
    # Helm dengan tanduk
    pygame.draw.ellipse(karakter_surface, (40, 40, 40),
                       (tengah_x - int(22 * skala), tengah_y - int(45 * skala),
                        int(44 * skala), int(30 * skala)))
    
    # Tanduk kiri
    pygame.draw.polygon(karakter_surface, (80, 0, 0), [
        (tengah_x - int(20 * skala), tengah_y - int(42 * skala)),
        (tengah_x - int(30 * skala), tengah_y - int(55 * skala)),
        (tengah_x - int(18 * skala), tengah_y - int(48 * skala))
    ])
    pygame.draw.polygon(karakter_surface, (120, 0, 0), [
        (tengah_x - int(30 * skala), tengah_y - int(55 * skala)),
        (tengah_x - int(35 * skala), tengah_y - int(60 * skala)),
        (tengah_x - int(28 * skala), tengah_y - int(58 * skala))
    ])
    
    # Tanduk kanan
    pygame.draw.polygon(karakter_surface, (80, 0, 0), [
        (tengah_x + int(20 * skala), tengah_y - int(42 * skala)),
        (tengah_x + int(30 * skala), tengah_y - int(55 * skala)),
        (tengah_x + int(18 * skala), tengah_y - int(48 * skala))
    ])
    pygame.draw.polygon(karakter_surface, (120, 0, 0), [
        (tengah_x + int(30 * skala), tengah_y - int(55 * skala)),
        (tengah_x + int(35 * skala), tengah_y - int(60 * skala)),
        (tengah_x + int(28 * skala), tengah_y - int(58 * skala))
    ])
    
    # Visor helm (T-shape)
    pygame.draw.rect(karakter_surface, (20, 20, 20),
                    (tengah_x - int(8 * skala), tengah_y - int(32 * skala),
                     int(16 * skala), int(4 * skala)))
    pygame.draw.rect(karakter_surface, (20, 20, 20),
                    (tengah_x - int(2 * skala), tengah_y - int(32 * skala),
                     int(4 * skala), int(12 * skala)))
    
    # Mata menyala merah (intimidating)
    mata_kiri_x = int(tengah_x - 10 * skala)
    mata_kanan_x = int(tengah_x + 10 * skala)
    mata_y = int(tengah_y - 28 * skala)
    
    # Glow effect
    for glow in range(3, 0, -1):
        alpha = 80 * glow
        pygame.draw.circle(karakter_surface, (255, 0, 0, alpha),
                          (mata_kiri_x, mata_y), int((4 + glow * 2) * skala))
        pygame.draw.circle(karakter_surface, (255, 0, 0, alpha),
                          (mata_kanan_x, mata_y), int((4 + glow * 2) * skala))
    
    # Mata merah menyala
    pygame.draw.circle(karakter_surface, (255, 50, 0), (mata_kiri_x, mata_y), int(5 * skala))
    pygame.draw.circle(karakter_surface, (255, 255, 0), (mata_kiri_x, mata_y), int(2 * skala))
    
    pygame.draw.circle(karakter_surface, (255, 50, 0), (mata_kanan_x, mata_y), int(5 * skala))
    pygame.draw.circle(karakter_surface, (255, 255, 0), (mata_kanan_x, mata_y), int(2 * skala))
    
    # Scar di helm
    pygame.draw.line(karakter_surface, (150, 150, 150),
                    (tengah_x + int(12 * skala), tengah_y - int(35 * skala)),
                    (tengah_x + int(18 * skala), tengah_y - int(25 * skala)), 2)
    
    # Flip horizontal jika perlu
    if flip:
        karakter_surface = pygame.transform.flip(karakter_surface, True, False)
    
    # Rotasi
    karakter_rotasi = pygame.transform.rotate(karakter_surface, rotasi)
    
    # Dapatkan rect untuk posisi
    rect = karakter_rotasi.get_rect(center=(x, y))
    
    # Gambar ke layar
    layar.blit(karakter_rotasi, rect)

def gambar_karakter(x, y, rotasi, skala, flip, warna_badan, warna_kepala, dengan_pedang=False):
    """Menggambar karakter musuh (versi lama)"""
    ukuran = int(60 * skala)
    karakter_surface = pygame.Surface((ukuran * 3, ukuran * 3), pygame.SRCALPHA)
    
    tengah_x = ukuran * 1.5
    tengah_y = ukuran * 1.5
    
    # Pedang
    if dengan_pedang:
        pygame.draw.rect(karakter_surface, COKLAT,
                        (tengah_x + int(25 * skala), tengah_y - int(5 * skala),
                         int(15 * skala), int(8 * skala)))
        pygame.draw.polygon(karakter_surface, (200, 200, 200), [
            (tengah_x + int(40 * skala), tengah_y - int(8 * skala)),
            (tengah_x + int(70 * skala), tengah_y - int(1 * skala)),
            (tengah_x + int(40 * skala), tengah_y + int(6 * skala))
        ])
        pygame.draw.polygon(karakter_surface, PUTIH, [
            (tengah_x + int(65 * skala), tengah_y - int(1 * skala)),
            (tengah_x + int(70 * skala), tengah_y - int(1 * skala)),
            (tengah_x + int(67 * skala), tengah_y + int(2 * skala))
        ])
    
    # Kepala
    pygame.draw.circle(karakter_surface, warna_kepala, 
                      (int(tengah_x), int(tengah_y - 20 * skala)), int(15 * skala))
    
    # Mata
    mata_kiri = (int(tengah_x - 5 * skala), int(tengah_y - 22 * skala))
    mata_kanan = (int(tengah_x + 5 * skala), int(tengah_y - 22 * skala))
    pygame.draw.circle(karakter_surface, HITAM, mata_kiri, int(3 * skala))
    pygame.draw.circle(karakter_surface, HITAM, mata_kanan, int(3 * skala))
    
    # Senyum
    pygame.draw.arc(karakter_surface, HITAM, 
                    (tengah_x - int(8 * skala), tengah_y - 20 * skala, 
                     int(16 * skala), int(10 * skala)), 
                    math.pi, 2 * math.pi, 2)
    
    # Badan
    pygame.draw.rect(karakter_surface, warna_badan, 
                     (tengah_x - int(12 * skala), tengah_y - 5 * skala, 
                      int(24 * skala), int(25 * skala)))
    
    # Tangan
    pygame.draw.rect(karakter_surface, warna_kepala, 
                     (tengah_x - int(20 * skala), tengah_y, 
                      int(8 * skala), int(20 * skala)))
    pygame.draw.rect(karakter_surface, warna_kepala, 
                     (tengah_x + int(12 * skala), tengah_y, 
                      int(8 * skala), int(20 * skala)))
    
    # Kaki
    pygame.draw.rect(karakter_surface, COKLAT, 
                     (tengah_x - int(10 * skala), tengah_y + 20 * skala, 
                      int(8 * skala), int(15 * skala)))
    pygame.draw.rect(karakter_surface, COKLAT, 
                     (tengah_x + int(2 * skala), tengah_y + 20 * skala, 
                      int(8 * skala), int(15 * skala)))
    
    if flip:
        karakter_surface = pygame.transform.flip(karakter_surface, True, False)
    
    karakter_rotasi = pygame.transform.rotate(karakter_surface, rotasi)
    rect = karakter_rotasi.get_rect(center=(x, y))
    layar.blit(karakter_rotasi, rect)

def tampilkan_info():
    """Menampilkan informasi kontrol dan status"""
    font = pygame.font.Font(None, 24)
    font_kecil = pygame.font.Font(None, 20)
    font_besar = pygame.font.Font(None, 48)
    
    # Score besar di tengah atas
    score_text = font_besar.render(f"SCORE: {score}", True, (255, 215, 0))
    score_rect = score_text.get_rect(center=(LEBAR // 2, 40))
    pygame.draw.rect(layar, (0, 0, 0, 100), score_rect.inflate(20, 10))
    layar.blit(score_text, score_rect)
    
    # Combo
    if combo > 1:
        combo_text = font.render(f"COMBO x{combo}!", True, (255, 100, 0))
        layar.blit(combo_text, (LEBAR // 2 - 60, 85))
    
    # Judul kontrol
    judul = font.render("Kontrol:", True, HITAM)
    layar.blit(judul, (10, 10))
    
    # Kontrol
    kontrol = [
        "W/A/S/D - Gerak",
        "Q/E - Putar",
        "Z/X - Skala",
        "C - Cermin",
        "SPASI - Serang",
        "R - Reset"
    ]
    
    y_pos = 35
    for teks in kontrol:
        render = font_kecil.render(teks, True, HITAM)
        layar.blit(render, (10, y_pos))
        y_pos += 18
    
    # Status
    status = [
        f"Pos: ({int(pos_x)},{int(pos_y)})",
        f"Rotasi: {int(rotasi)}°",
        f"Skala: {skala:.1f}x"
    ]
    
    y_pos = TINGGI - 80
    status_judul = font.render("Status:", True, HITAM)
    layar.blit(status_judul, (10, y_pos - 25))
    
    for teks in status:
        render = font_kecil.render(teks, True, HITAM)
        layar.blit(render, (10, y_pos))
        y_pos += 18
    
    # Info tips
    tips = font_kecil.render("Tips: Kejar musuh dengan pedang!", True, (100, 50, 150))
    layar.blit(tips, (LEBAR - 250, TINGGI - 25))

def gambar_partikel():
    """Menggambar efek partikel"""
    global partikel
    for p in partikel[:]:
        p['y'] -= p['vy']
        p['x'] += p['vx']
        p['life'] -= 1
        p['size'] -= 0.1
        
        if p['life'] <= 0 or p['size'] <= 0:
            partikel.remove(p)
        else:
            alpha = int(255 * (p['life'] / 30))
            s = pygame.Surface((int(p['size'] * 2), int(p['size'] * 2)), pygame.SRCALPHA)
            pygame.draw.circle(s, (*p['color'], alpha), (int(p['size']), int(p['size'])), int(p['size']))
            layar.blit(s, (int(p['x']), int(p['y'])))

# Loop utama
berjalan = True
while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False
    
    # Input keyboard
    tombol = pygame.key.get_pressed()
    
    # 1. Gerak dengan Dash (W/A/S/D)
    if tombol[pygame.K_w]:
        pos_y -= kecepatan * 4
    if tombol[pygame.K_s]:
        pos_y += kecepatan * 4
    if tombol[pygame.K_a]:
        pos_x -= kecepatan * 4
    if tombol[pygame.K_d]:
        pos_x += kecepatan * 4
    
    # 2. Rotasi (Q/E)
    if tombol[pygame.K_q]:
        rotasi += 2
    if tombol[pygame.K_e]:
        rotasi -= 2
    
    # 3. Skala (Z/X)
    if tombol[pygame.K_z]:
        skala = min(skala + 0.02, 3.0)
    if tombol[pygame.K_x]:
        skala = max(skala - 0.02, 0.3)
    
    # 4. Flip Horizontal (C)
    if tombol[pygame.K_c]:
        pygame.time.wait(200)
        flip_horizontal = not flip_horizontal
    
    # 5. Pedang (SPASI)
    if tombol[pygame.K_SPACE]:
        pedang_aktif = True
    else:
        pedang_aktif = False
    
    # Reset (R)
    if tombol[pygame.K_r]:
        pos_x = 400
        pos_y = 300
        rotasi = 0
        skala = 1.0
        flip_horizontal = False
        pedang_aktif = False
        score = 0
        combo = 0
    
    # Batasi posisi
    pos_x = max(50, min(pos_x, LEBAR - 50))
    pos_y = max(50, min(pos_y, TINGGI - 50))
    
    # Update animasi
    frame_animasi += 1
    
    # Efek bouncing
    offset_lompat = math.sin(frame_animasi * 0.15) * 5
    
    # AI Musuh
    musuh_x += musuh_arah_x
    musuh_y += musuh_arah_y
    
    if musuh_x <= 100 or musuh_x >= LEBAR - 100:
        musuh_arah_x *= -1
        musuh_flip = not musuh_flip
    if musuh_y <= 100 or musuh_y >= TINGGI - 100:
        musuh_arah_y *= -1
    
    if pygame.time.get_ticks() % 100 < 50:
        musuh_pedang_aktif = True
    else:
        musuh_pedang_aktif = False
    
    musuh_rotasi += 0.3
    
    # Deteksi tabrakan
    jarak = math.sqrt((pos_x - musuh_x)**2 + (pos_y - musuh_y)**2)
    
    if hit_cooldown > 0:
        hit_cooldown -= 1
    
    if jarak < 60 and pedang_aktif and hit_cooldown == 0:
        hit_cooldown = 30
        
        if pygame.time.get_ticks() - waktu_combo < 2000:
            combo += 1
        else:
            combo = 1
        waktu_combo = pygame.time.get_ticks()
        
        score += 10 * combo
        
        # Partikel saat hit
        for _ in range(15):
            partikel.append({
                'x': musuh_x,
                'y': musuh_y,
                'vx': random.uniform(-3, 3),
                'vy': random.uniform(1, 5),
                'life': 30,
                'size': random.uniform(3, 8),
                'color': random.choice([(255, 200, 0), (255, 150, 0), (255, 100, 100)])
            })
        
        musuh_x = random.randint(150, LEBAR - 150)
        musuh_y = random.randint(150, TINGGI - 150)
        musuh_arah_x = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        musuh_arah_y = random.choice([-1, 1]) * random.uniform(0.3, 1)
    
    if pygame.time.get_ticks() - waktu_combo > 2000:
        combo = 0
    
    # Gambar semua
    gambar_latar()
    
    # Gambar musuh
    gambar_karakter(musuh_x, musuh_y, musuh_rotasi, musuh_skala, musuh_flip, 
                   (50, 50, 50), (200, 50, 50), musuh_pedang_aktif)
    
    # Gambar pemain LUCU
    gambar_karakter_lucu(pos_x, pos_y, rotasi, skala, flip_horizontal, 
                        frame_animasi, offset_lompat, pedang_aktif)
    
    # Efek visual saat hit
    if hit_cooldown > 25:
        pygame.draw.circle(layar, (255, 255, 0), (int(musuh_x), int(musuh_y)), 40, 3)
        pygame.draw.circle(layar, (255, 200, 0), (int(musuh_x), int(musuh_y)), 50, 2)
    
    # Gambar partikel
    gambar_partikel()
    
    tampilkan_info()
    
    # Update layar
    pygame.display.flip()
    clock.tick(60)

pygame.quit()  