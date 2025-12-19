import pygame
import math

# --- Setup Pygame ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arena Pertandingan Transformasi 2D")
clock = pygame.time.Clock()

# Definisi Warna Baru untuk Nuansa Pertandingan
DARK_GRAY = (50, 50, 50)         # Latar belakang arena gelap
ARENA_COLOR = (100, 100, 100)    # Warna lantai arena/batas
WHITE = (255, 255, 255)          # Warna teks UI
RED = (255, 0, 0)
BLUE_PLAYER = (100, 100, 255)    # Warna pemain
ENEMY_COLOR = (255, 150, 150)    # Warna lawan
FONT = pygame.font.Font(None, 24)

# Origin visual dan skala
ORIGIN_X, ORIGIN_Y = WIDTH // 4, HEIGHT // 2
SCALE_FACTOR = 15
ENEMY_SPEED = 0.05 
SCALE_STEP = 1.2 

# Fungsi Utility (Sama seperti sebelumnya)
def world_to_screen(x, y):
    return ORIGIN_X + x * SCALE_FACTOR, ORIGIN_Y - y * SCALE_FACTOR

def draw_axes():
    # Sumbu tidak lagi digambar karena fokus pada arena
    pass 

# --- Status Karakter & Animasi (Sama seperti sebelumnya) ---
char_x, char_y = 10, 5
target_x, target_y = 10, 5
char_scale = 1.0 
is_flipped = False
current_sword_angle = 0
target_sword_angle = 0
frame_index = 0

# --- Status Lawan (Sama seperti sebelumnya) ---
enemy_x, enemy_y = 40, 5
enemy_hit_status = False
last_hit_time = 0

# --- Game Loop ---
running = True
while running:
    # --- PENGGAMBARAN LATAR BELAKANG BARU ---
    screen.fill(DARK_GRAY)
    
    # Gambar lantai arena sederhana
    # Menggunakan area tertentu dari layar sebagai "ring"
    pygame.draw.rect(screen, ARENA_COLOR, (ORIGIN_X - 100, ORIGIN_Y - 200, WIDTH - ORIGIN_X, HEIGHT))

    draw_axes()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                target_x += 20
            elif event.key == pygame.K_2:
                target_sword_angle += 30
                distance = math.sqrt((char_x - enemy_x)**2 + (char_y - enemy_y)**2)
                if distance < (20 * char_scale):
                    enemy_hit_status = True
                    last_hit_time = pygame.time.get_ticks()
            elif event.key == pygame.K_3:
                char_scale *= SCALE_STEP
            elif event.key == pygame.K_4:
                is_flipped = not is_flipped
            elif event.key == pygame.K_5:
                char_scale /= SCALE_STEP
                if char_scale < 0.1:
                    char_scale = 0.1

    # --- Update Logika ---
    char_x += (target_x - char_x) * 0.1
    char_y += (target_y - char_y) * 0.1
    angle_diff = (target_sword_angle - current_sword_angle + 180) % 360 - 180
    current_sword_angle += angle_diff * 0.2
    if pygame.time.get_ticks() - last_hit_time > 500:
        enemy_hit_status = False

    # Logika Pergerakan Lawan
    if enemy_x < char_x:
        enemy_x += ENEMY_SPEED
    elif enemy_x > char_x:
        enemy_x -= ENEMY_SPEED
    if enemy_y < char_y:
        enemy_y += ENEMY_SPEED
    elif enemy_y > char_y:
        enemy_y -= ENEMY_SPEED
    
    # Update frame animasi
    # (Kode sprite sheet dihapus dari sini agar kode lebih sederhana, kembali ke lingkaran)


    # --- Penggambaran Lawan ---
    enemy_screen_x, enemy_screen_y = world_to_screen(enemy_x, enemy_y)
    enemy_draw_color = RED if enemy_hit_status else ENEMY_COLOR
    pygame.draw.circle(screen, enemy_draw_color, (int(enemy_screen_x), int(enemy_screen_y)), 15)

    # --- Penggambaran Karakter (Kembali ke Lingkaran karena tidak ada file gambar) ---
    screen_x, screen_y = world_to_screen(char_x, char_y)
    radius = int(10 * char_scale)
    pygame.draw.circle(screen, BLUE_PLAYER, (int(screen_x), int(screen_y)), radius)
    
    # Gambar "pedang" lagi karena kita tidak pakai sprite sheet
    sword_length = radius * 2
    angle_rad = math.radians(current_sword_angle)
    flip_multiplier = -1 if is_flipped else 1
    sword_end_x = screen_x + math.cos(angle_rad) * sword_length * flip_multiplier
    sword_end_y = screen_y - math.sin(angle_rad) * sword_length
    pygame.draw.line(screen, RED, (screen_x, screen_y), (sword_end_x, sword_end_y), 5)


    # --- Teks UI (Warna Putih agar kontras dengan background gelap) ---
    screen.blit(FONT.render(f"Posisi: ({char_x:.1f}, {char_y:.1f}) | Skala: {char_scale:.2f}x", True, WHITE), (10, 10))
    screen.blit(FONT.render(f"Status Lawan: {'Kena Pukul!' if enemy_hit_status else 'Mengejar Anda!'}", True, WHITE), (10, 30))
    screen.blit(FONT.render("Kontrol: 1 (Dash), 2 (Pukul), 3 (Perbesar), 4 (Cermin), 5 (Perkecil)", True, WHITE), (10, 50))

    # Update layar
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
