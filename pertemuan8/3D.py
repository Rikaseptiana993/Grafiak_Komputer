import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math, random, time

# =====================
# KUBUS
# =====================
vertices = (
    (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
    (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
)

surfaces = (
    (0,1,2,3),(4,5,6,7),
    (0,1,5,4),(2,3,7,6),
    (1,2,6,5),(0,3,7,4)
)

def cube(color):
    glColor3fv(color)
    glBegin(GL_QUADS)
    for s in surfaces:
        for v in s:
            glVertex3fv(vertices[v])
    glEnd()

# =====================
# LANTAI
# =====================
def floor():
    glColor3f(0.4,0.4,0.4)
    glBegin(GL_QUADS)
    glVertex3f(-50,-1,-50)
    glVertex3f(-50,-1,50)
    glVertex3f(50,-1,50)
    glVertex3f(50,-1,-50)
    glEnd()

# =====================
# SENJATA DETAIL
# =====================
def detailed_gun():
    glPushMatrix()
    glScalef(0.35,0.2,1.6)
    cube((0.12,0.12,0.12))
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,1.9)
    glScalef(0.12,0.12,1.4)
    cube((0.2,0.2,0.2))
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,-0.55,0.4)
    glRotatef(-15,1,0,0)
    glScalef(0.25,0.6,0.35)
    cube((0.1,0.1,0.1))
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,-1.4)
    glScalef(0.35,0.25,0.8)
    cube((0.15,0.15,0.15))
    glPopMatrix()

# =====================
# PLAYER
# =====================
def player_model():
    glPushMatrix()
    glTranslatef(0,1,0)
    glScalef(0.8,1.2,0.4)
    cube((0.2,0.5,1))
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,2.2,0)
    glScalef(0.4,0.4,0.4)
    cube((1,0.8,0.6))
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.7,1.4,0.3)
    glRotatef(-90,1,0,0)
    glScalef(0.25,0.8,0.25)
    cube((0.2,0.5,1))

    glTranslatef(0,0,-2.4)
    glRotatef(90,1,0,0)
    detailed_gun()
    glPopMatrix()

# =====================
# MUSUH
# =====================
class Enemy:
    def __init__(self, speed):
        self.speed = speed
        self.respawn()

    def respawn(self):
        self.x = random.randint(-20,20)
        self.z = random.randint(-20,20)

    def update(self, px, pz):
        dx = px - self.x
        dz = pz - self.z
        dist = math.hypot(dx, dz)
        if dist > 0.5:
            self.x += dx/dist * self.speed
            self.z += dz/dist * self.speed
        return dist

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x,0,self.z)
        cube((1,0,0))
        glPopMatrix()

# =====================
# LEDAKAN
# =====================
class Explosion:
    def __init__(self, x, y, z):
        self.particles = []
        for _ in range(25):
            self.particles.append([
                x, y, z,
                random.uniform(-0.2,0.2),
                random.uniform(0.1,0.4),
                random.uniform(-0.2,0.2),
                random.randint(20,30)
            ])

    def update(self):
        for p in self.particles[:]:
            p[0] += p[3]
            p[1] += p[4]
            p[2] += p[5]
            p[4] -= 0.02
            p[6] -= 1
            if p[6] <= 0:
                self.particles.remove(p)

    def draw(self):
        for p in self.particles:
            life = p[6] / 30
            glColor3f(1, life, 0)
            glPushMatrix()
            glTranslatef(p[0],p[1],p[2])
            glScalef(0.15,0.15,0.15)
            cube((1,life,0))
            glPopMatrix()

    def is_done(self):
        return len(self.particles) == 0

# =====================
# MAIN GAME
# =====================
def main():
    pygame.init()
    pygame.display.set_mode((900,600), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("TPS Mini Game + Explosion")

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 900/600, 0.1, 200)
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.1,0.1,0.15,1)

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    px, pz = 0,0
    yaw = 0
    bullets = []

    score = 0
    wave = 1
    player_hp = 100

    enemies = []
    explosions = []

    def spawn_wave():
        enemies.clear()
        for _ in range(wave * 3):
            enemies.append(Enemy(0.02 + wave*0.005))

    spawn_wave()
    clock = pygame.time.Clock()
    game_over = False

    while True:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); quit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit(); quit()
                if e.key == K_r:
                    score = 0
                    wave = 1
                    player_hp = 100
                    spawn_wave()
                    explosions.clear()
                    game_over = False
            if e.type == MOUSEMOTION:
                yaw += e.rel[0]*0.2
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and not game_over:
                dx = math.sin(math.radians(yaw))
                dz = -math.cos(math.radians(yaw))
                bullets.append([px,1.4,pz,dx*0.6,dz*0.6])

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                px += math.sin(math.radians(yaw))*0.15
                pz -= math.cos(math.radians(yaw))*0.15

        # UPDATE ENEMY
        for enemy in enemies[:]:
            dist = enemy.update(px,pz)
            if dist < 1:
                player_hp -= 1
                if player_hp <= 0:
                    game_over = True

        # BULLET & LEDAKAN
        for b in bullets[:]:
            b[0] += b[3]
            b[2] += b[4]
            for enemy in enemies[:]:
                if math.hypot(b[0]-enemy.x, b[2]-enemy.z) < 1:
                    score += 10
                    explosions.append(Explosion(enemy.x,1,enemy.z))
                    enemies.remove(enemy)
                    bullets.remove(b)
                    break

        if not enemies and not game_over:
            wave += 1
            spawn_wave()

        for ex in explosions[:]:
            ex.update()
            if ex.is_done():
                explosions.remove(ex)

        # RENDER
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        cam_x = px - math.sin(math.radians(yaw))*8
        cam_z = pz + math.cos(math.radians(yaw))*8
        gluLookAt(cam_x,5,cam_z, px,1.5,pz, 0,1,0)

        floor()

        for enemy in enemies:
            enemy.draw()

        for ex in explosions:
            ex.draw()

        glPushMatrix()
        glTranslatef(px,0,pz)
        player_model()
        glPopMatrix()

        for b in bullets:
            glPushMatrix()
            glTranslatef(b[0],b[1],b[2])
            glScalef(0.15,0.15,0.15)
            cube((1,1,0))
            glPopMatrix()

        pygame.display.flip()
        pygame.display.set_caption(
            f"Score:{score} | Wave:{wave} | HP:{player_hp}"
        )

if __name__ == "__main__":
    main()
