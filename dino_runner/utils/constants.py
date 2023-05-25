import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Sonic Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/Jump.wav"))
LAND_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/Land.wav"))
DUCK_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/DropDash.wav"))
RING_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/Ring.wav"))
DESTROY = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/Destroy.wav"))
DEATH_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/Hurt.wav"))

MENU_BLEEP = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/MenuBleep.wav"))

BG_SOUND = pygame.mixer.music.load(os.path.join(IMG_DIR, "Sounds/GHZAct1.mp3"))

YELLOW = (255, 255, 0)

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "ICON.png"))
icon_death = pygame.image.load(os.path.join(IMG_DIR, "Other/DEATH.png"))
ICON_DEATH = pygame.transform.scale(icon_death, (45 * 3, 45 * 3))
start_menu = pygame.image.load(os.path.join(IMG_DIR, "Other/Telainicial.png"))
START_MENU = pygame.transform.scale(start_menu, (250 * 1.2, 250 * 1.2))

RUN = pygame.image.load(os.path.join(IMG_DIR, "Dino/RUN.png"))

RUNNING = []
for i in range(8):
    img_run = RUN.subsurface((i * 45, 0), (45, 45))
    img_run = pygame.transform.scale(img_run, (45 * 2, 45 * 2))
    RUNNING.append(img_run)

RUN_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/RUN-SHIELD.png"))

RUNNING_SHIELD = []
for i in range(8):
    img_run_shield = RUN_SHIELD.subsurface((i * 45, 0), (45, 45))
    img_run_shield = pygame.transform.scale(img_run_shield, (45 * 2, 45 * 2))
    RUNNING_SHIELD.append(img_run_shield)

JUMP = pygame.image.load(os.path.join(IMG_DIR, "Dino/JUMP.png"))
JUMPING = []
for i in range(16):
    img_jump = JUMP.subsurface((i * 45, 0), (45, 45))
    img_jump = pygame.transform.scale(img_jump, (45 * 2, 45 * 2))
    JUMPING.append(img_jump)

jump_shield = pygame.image.load(os.path.join(IMG_DIR, "Dino/JUMP-SHIELD.png"))
JUMPING_SHIELD = []
for i in range(16):
    img_jump_shield = jump_shield.subsurface((i * 45, 0), (45, 45))
    img_jump_shield = pygame.transform.scale(img_jump_shield, (45 * 2, 45 * 2))
    JUMPING_SHIELD.append(img_jump_shield)

duck = pygame.image.load(os.path.join(IMG_DIR, "Dino/BEND-OVER.png"))
DUCKING = []
for i in range(16):
    img_duck = duck.subsurface((i * 45, 0), (45, 45))
    img_duck = pygame.transform.scale(img_duck, (45 * 2, 45 * 2))
    DUCKING.append(img_duck)


duck_shield = pygame.image.load(os.path.join(IMG_DIR, "Dino/BEND-OVER-SHIELD.png"))
DUCKING_SHIELD = []
for i in range(16):
    img_duck_shield = duck_shield.subsurface((i * 45, 0), (45, 45))
    img_duck_shield = pygame.transform.scale(img_duck_shield, (45 * 2, 45 * 2))
    DUCKING_SHIELD.append(img_duck_shield)

small_obstacle = pygame.image.load(os.path.join(IMG_DIR, "Cactus/SMALL-OBSTACLE.png"))
SMALL_CACTUS = []
for i in range(3):
    img_small = small_obstacle.subsurface((i * 25, 0), (25, 25))
    img_small = pygame.transform.scale(img_small, (25 * 3, 25 * 3))
    SMALL_CACTUS.append(img_small)

large_obstacle = pygame.image.load(os.path.join(IMG_DIR, "Cactus/LARGE-OBSTACLE.png"))
LARGE_CACTUS = []
for i in range(3):
    img_large = large_obstacle.subsurface((i * 30, 0), (30, 30))
    img_large = pygame.transform.scale(img_large, (30 * 3, 30 * 3))
    LARGE_CACTUS.append(img_large)

bird = pygame.image.load(os.path.join(IMG_DIR, "Bird/ENEMY.png"))

BIRD = []
for i in range(9):
    img_run = bird.subsurface((i * 45, 0), (45, 45))
    img_run = pygame.transform.scale(img_run, (45 * 2, 45 * 2))
    BIRD.append(img_run)


cloud = pygame.image.load(os.path.join(IMG_DIR, 'Other/NUVEM.png'))
CLOUD = pygame.transform.scale(cloud, (45 * 2, 45 * 2))

shield = pygame.image.load(os.path.join(IMG_DIR, 'Other/HYPER-RING.png'))
SHIELD = []
for i in range(16):
    img_run = shield.subsurface((i * 45, 0), (45, 45))
    img_run = pygame.transform.scale(img_run, (45 * 2, 45 * 2))
    SHIELD.append(img_run)

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/FLOOR.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "Super Saiyajin"
