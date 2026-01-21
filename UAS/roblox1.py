from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Variabel game
checkpoint_reached = 0
coins_collected = 0
game_started = False

# Skybox
sky = Sky()

# Player dengan kemampuan seperti Roblox
class RobloxPlayer(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.jump_height = 2.5  # Lompatan lebih tinggi
        self.jump_up_duration = 0.5
        self.fall_after = 0.35
        self.speed = 5
        self.can_double_jump = True
        self.double_jumped = False
        
    def jump(self):
        if not self.grounded and self.can_double_jump and not self.double_jumped:
            # Double jump
            self.double_jumped = True
            self.y += self.jump_height * 0.7
            self.animate_y(self.y + self.jump_height * 0.7, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)
            invoke(self.start_fall, delay=self.fall_after)
        elif self.grounded:
            super().jump()
            self.double_jumped = False
            
    def update(self):
        super().update()
        if self.grounded:
            self.double_jumped = False
            
        # Jatuh ke bawah = respawn
        if self.y < -20:
            self.position = spawn_point.position + Vec3(0, 2, 0)

# Spawn point
spawn_point = Entity(
    model='cube',
    color=color.green,
    scale=(6, 0.5, 6),
    position=(0, 0, 0),
    collider='box'
)

# Buat platform parkour - TANTANGAN DATAR (TIDAK TINGGI)
platforms = []

# Platform 1 - Tangga rendah
for i in range(10):
    plat = Entity(
        model='cube',
        color=color.blue,
        scale=(4.5, 0.5, 4.5),  # Platform sangat besar
        position=(0, i * 0.3, -4 - i * 1.5),  # Naik sangat pelan
        collider='box'
    )
    platforms.append(plat)

# Platform datar penghubung 1
for i in range(5):
    plat = Entity(
        model='cube',
        color=color.light_gray,
        scale=(4.5, 0.5, 4.5),
        position=(0, 3, -20 - i * 2),
        collider='box'
    )
    platforms.append(plat)

# Platform 2 - Zig-zag DATAR
for i in range(10):
    x_pos = 3 if i % 2 == 0 else -3
    plat = Entity(
        model='cube',
        color=color.orange,
        scale=(4, 0.5, 4),
        position=(x_pos, 3, -30 - i * 1.5),  # Tetap di ketinggian yang sama
        collider='box'
    )
    platforms.append(plat)

# Platform datar penghubung 2
for i in range(5):
    plat = Entity(
        model='cube',
        color=color.light_gray,
        scale=(4.5, 0.5, 4.5),
        position=(0, 3, -46 - i * 2),
        collider='box'
    )
    platforms.append(plat)

# Platform 3 - Platform bergerak DATAR
moving_platforms = []
for i in range(6):
    plat = Entity(
        model='cube',
        color=color.violet,
        scale=(4.5, 0.5, 4.5),
        position=(-4, 3.5, -58 - i * 2),  # Naik sedikit saja
        collider='box'
    )
    plat.direction = 1
    plat.start_x = plat.x
    plat.speed = 1.2  # Bergerak lambat
    moving_platforms.append(plat)
    platforms.append(plat)

# Platform datar penghubung 3
for i in range(5):
    plat = Entity(
        model='cube',
        color=color.light_gray,
        scale=(4.5, 0.5, 4.5),
        position=(0, 4, -72 - i * 2),
        collider='box'
    )
    platforms.append(plat)

# Platform 4 - Platform sedang DATAR
for i in range(10):
    plat = Entity(
        model='cube',
        color=color.yellow,
        scale=(3.5, 0.5, 3.5),
        position=(random.uniform(-3, 3), 4, -84 - i * 1.3),  # Tetap rata
        collider='box'
    )
    platforms.append(plat)

# Platform datar penghubung 4
for i in range(4):
    plat = Entity(
        model='cube',
        color=color.light_gray,
        scale=(4.5, 0.5, 4.5),
        position=(0, 4, -98 - i * 2),
        collider='box'
    )
    platforms.append(plat)

# Platform 5 - Rotating platform DATAR
rotating_platforms = []
for i in range(5):
    plat = Entity(
        model='cube',
        color=color.red,
        scale=(5.5, 0.5, 2.5),  # Lebih lebar
        position=(0, 4.5, -108 - i * 2.5),  # Naik sedikit
        collider='box'
    )
    rotating_platforms.append(plat)
    platforms.append(plat)

# Platform akhir menuju finish
for i in range(6):
    plat = Entity(
        model='cube',
        color=color.cyan,
        scale=(4.5, 0.5, 4.5),
        position=(0, 5 + i * 0.2, -122 - i * 1.5),  # Naik sangat pelan
        collider='box'
    )
    platforms.append(plat)

# Finish platform
finish_platform = Entity(
    model='cube',
    color=color.gold,
    scale=(8, 0.5, 8),  # Platform finish sangat besar
    position=(0, 6, -132),
    collider='box'
)

# Checkpoint - POSISI RENDAH
checkpoints = []
checkpoint_positions = [
    Vec3(0, 3, -30),
    Vec3(0, 3.5, -70),
    Vec3(0, 4.5, -108),
]

for i, pos in enumerate(checkpoint_positions):
    cp = Entity(
        model='cube',
        color=color.lime,
        scale=(5, 6, 0.5),
        position=pos,
        collider='box',
        alpha=0.5
    )
    cp.checkpoint_id = i
    checkpoints.append(cp)

# Coins - POSISI RENDAH
coins = []
coin_positions = [
    Vec3(0, 1.5, -8), Vec3(3, 3.5, -35), Vec3(-3, 3.5, -40),
    Vec3(-4, 4, -65), Vec3(0, 4.5, -90), Vec3(2, 4.5, -95),
    Vec3(-2, 5, -115), Vec3(0, 5.5, -125)
]

for pos in coin_positions:
    coin = Entity(
        model='sphere',
        color=color.yellow,
        scale=0.7,  # Koin lebih besar
        position=pos,
        collider='sphere'
    )
    coin.animate_rotation_y(360, duration=2, loop=True)
    coin.animate_y(pos.y + 0.3, duration=1, curve=curve.in_out_sine, loop=True)
    coins.append(coin)

# Decoration - Walls lebih rendah
wall1 = Entity(
    model='cube',
    color=color.gray,
    scale=(1, 12, 140),
    position=(-10, 5, -66)
)
wall2 = Entity(
    model='cube',
    color=color.gray,
    scale=(1, 12, 140),
    position=(10, 5, -66)
)

# Player
player = RobloxPlayer()
player.position = spawn_point.position + Vec3(0, 2, 0)
player.cursor.visible = False

# Camera lebih jauh
camera.fov = 90

# UI
title_text = Text(
    text='ROBLOX STYLE OBBY - MODE SANTAI',
    position=(0, 0.45),
    origin=(0, 0),
    scale=2.5,
    color=color.white,
    background=True
)

info_text = Text(
    text='WASD: Gerak | SPACE: Lompat (2x) | Mouse: Lihat | ESC: Keluar',
    position=(0, 0.4),
    origin=(0, 0),
    scale=1.2,
    color=color.white,
    background=True
)

coins_text = Text(
    text='Koin: 0/8',
    position=(-0.85, 0.45),
    scale=2,
    color=color.yellow,
    background=True
)

checkpoint_text = Text(
    text='Checkpoint: 0/3',
    position=(-0.85, 0.4),
    scale=1.5,
    color=color.lime,
    background=True
)

win_text = Text(
    text='',
    position=(0, 0),
    origin=(0, 0),
    scale=3,
    color=color.gold,
    visible=False,
    background=True
)

# Update function
def update():
    global checkpoint_reached, coins_collected
    
    # Update moving platforms - SANGAT LAMBAT
    for plat in moving_platforms:
        plat.x += plat.direction * plat.speed * time.dt
        if abs(plat.x - plat.start_x) > 2.5:  # Jarak gerak pendek
            plat.direction *= -1
    
    # Update rotating platforms - SANGAT LAMBAT
    for plat in rotating_platforms:
        plat.rotation_y += 15 * time.dt  # Rotasi sangat lambat
    
    # Check checkpoint collision
    for cp in checkpoints:
        if distance(player.position, cp.position) < 4:
            if cp.checkpoint_id > checkpoint_reached:
                checkpoint_reached = cp.checkpoint_id
                checkpoint_text.text = f'Checkpoint: {checkpoint_reached + 1}/3'
                cp.color = color.white
                spawn_point.position = cp.position
    
    # Check coin collision
    for coin in coins[:]:
        if coin.enabled and distance(player.position, coin.position) < 1.5:
            coin.enabled = False
            coin.visible = False
            coins_collected += 1
            coins_text.text = f'Koin: {coins_collected}/8'
    
    # Check finish
    if distance(player.position, finish_platform.position) < 5:
        win_text.text = f'🏆 SELAMAT! 🏆\n\nKamu menyelesaikan Obby!\nKoin terkumpul: {coins_collected}/8\n\nTekan R untuk main lagi'
        win_text.visible = True
        player.speed = 0

# Input
def input(key):
    global checkpoint_reached, coins_collected
    
    if key == 'escape':
        application.quit()
    
    if key == 'r' and win_text.visible:
        # Restart
        player.position = spawn_point.position + Vec3(0, 2, 0)
        player.speed = 5
        checkpoint_reached = 0
        coins_collected = 0
        win_text.visible = False
        
        # Reset checkpoints
        for cp in checkpoints:
            cp.color = color.lime
        
        # Reset coins
        for coin in coins:
            coin.enabled = True
            coin.visible = True
        
        checkpoint_text.text = 'Checkpoint: 0/3'
        coins_text.text = 'Koin: 0/8'

app.run()
