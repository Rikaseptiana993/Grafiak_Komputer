import pygame
import random
import sys
import math

pygame.init()

# ================= KONSTANTA =================
WIDTH, HEIGHT = 800, 600
GROUND_Y = HEIGHT - 40

WHITE = (255, 255, 255)
BLACK = (10, 10, 30)
RED = (255, 80, 80)
GREEN = (80, 255, 120)
BLUE = (80, 120, 255)
YELLOW = (255, 255, 120)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformasi Geometri 2D + Game Over")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

# ================= PLAYER =================
class Player:
    def __init__(self):
        self.w, self.h = 80, 20
        self.x = WIDTH // 2
        self.y = GROUND_Y - self.h
        self.speed = 7

    def move(self, dx):
        self.x += dx
        self.x = max(0, min(WIDTH - self.w, self.x))

    def get_surface(self):
        surf = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        pygame.draw.rect(surf, BLUE, (0, 0, self.w, self.h))
        pygame.draw.rect(surf, WHITE, (0, 0, self.w, self.h), 2)
        return surf

    def draw(self):
        surf = self.get_surface()
        screen.blit(surf, (self.x, self.y))

        # ===== REFLEKSI PLAYER =====
        refleksi = pygame.transform.flip(surf, False, True)
        refleksi.set_alpha(100)
        screen.blit(refleksi, (self.x, 2 * GROUND_Y - self.y))

# ================= OBJEK JATUH =================
class FallingObject:
    def __init__(self):
        self.base_size = 30
        self.x = random.randint(100, WIDTH - 100)
        self.y = -50

        self.speed_y = random.uniform(2, 4)
        self.angle = 0
        self.scale = 1.0
        self.scale_dir = 1
        self.time = random.uniform(0, 6)

        self.type = random.choice(["good", "bad"])

    def update(self):
        # ===== TRANSLASI =====
        self.y += self.speed_y
        self.x += math.sin(self.time) * 2
        self.time += 0.05

        # ===== ROTASI =====
        self.angle += 4

        # ===== SKALA =====
        self.scale += 0.01 * self.scale_dir
        if self.scale > 1.4 or self.scale < 0.6:
            self.scale_dir *= -1

    def get_surface(self):
        surf = pygame.Surface((self.base_size, self.base_size), pygame.SRCALPHA)
        if self.type == "good":
            pygame.draw.circle(surf, GREEN, (15, 15), 15)
        else:
            pygame.draw.rect(surf, RED, (0, 0, 30, 30))
        return surf

    def draw(self):
        surf = self.get_surface()

        # SKALA
        size = int(self.base_size * self.scale)
        surf = pygame.transform.scale(surf, (size, size))

        # ROTASI
        surf = pygame.transform.rotate(surf, self.angle)

        rect = surf.get_rect(center=(self.x, self.y))
        screen.blit(surf, rect)

        # REFLEKSI
        refleksi = pygame.transform.flip(surf, False, True)
        refleksi.set_alpha(80)
        refleksi_rect = refleksi.get_rect(center=(self.x, 2 * GROUND_Y - self.y))
        screen.blit(refleksi, refleksi_rect)

    def off_screen(self):
        return self.y > HEIGHT + 50

    def collide(self, player):
        return (
            self.y >= player.y and
            self.x > player.x and
            self.x < player.x + player.w
        )

# ================= MAIN =================
def main():
    player = Player()
    objects = []
    score = 0
    lives = 3
    spawn_timer = 0
    game_over = False

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                    return
                if event.key == pygame.K_ESCAPE:
                    running = False

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-player.speed)
            if keys[pygame.K_RIGHT]:
                player.move(player.speed)

            spawn_timer += 1
            if spawn_timer > 45:
                objects.append(FallingObject())
                spawn_timer = 0

            for obj in objects[:]:
                obj.update()
                if obj.collide(player):
                    if obj.type == "good":
                        score += 10
                    else:
                        lives -= 1
                        if lives <= 0:
                            game_over = True
                    objects.remove(obj)
                elif obj.off_screen():
                    objects.remove(obj)

        # ===== RENDER =====
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (0, GROUND_Y), (WIDTH, GROUND_Y), 2)

        player.draw()
        for obj in objects:
            obj.draw()

        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
        screen.blit(font.render(f"Lives: {lives}", True, WHITE), (10, 45))

        # ===== GAME OVER SCREEN =====
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            screen.blit(big_font.render("GAME OVER", True, RED), (260, 200))
            screen.blit(font.render(f"Final Score: {score}", True, WHITE), (310, 280))
            screen.blit(font.render("Press R to Restart", True, YELLOW), (290, 330))
            screen.blit(font.render("Press ESC to Exit", True, YELLOW), (300, 360))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

 m 