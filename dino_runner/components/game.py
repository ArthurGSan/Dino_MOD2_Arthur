import pygame
import os

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, CLOUD, IMG_DIR, ICON_DEATH, START_MENU, MENU_BLEEP
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.menu import Menu

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACK_GROUND = pygame.image.load(os.path.join(IMG_DIR, 'Other/Background-night.png')).convert()
BACK_GROUND = pygame.transform.scale(BACK_GROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 350
        self.score_rank = []
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.menu = Menu()

    def execute(self):
        self.running = True
        while self.running:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            if not self.playing:
                self.menu.show_menu(self, self.screen, self.score , self.death_count, self.score_rank)
        pygame.quit()
        exit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 10
        self.score = 0

        while self.playing:
            self.events()
            self.update()
            self.draw()

    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0 and self.score < 900:
            self.game_speed += 3

    def update_score_rank(self):
        self.score_rank.append(self.score + 1)
        if len(self.score_rank) > 0:
            index = len(self.score_rank) - 1
            last_element_index = index
            last_element = self.score_rank[index]
            index -= 1
            while index >= 0:
                if last_element > self.score_rank[index]:
                    self.score_rank[index], self.score_rank[last_element_index] = self.score_rank[last_element_index], self.score_rank[index]
                    last_element_index = index
                index -= 1
            if len(self.score_rank) >= 6:
                self.score_rank.pop(-1)

    def draw(self):
        self.clock.tick(FPS)
        screen.blit(BACK_GROUND, (0, 0))   
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg, 150))
        if self.x_pos_bg <= - image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        draw_message_component(
            f"Score: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50
       )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} ativo por {time_to_show} segundos",
                    self.screen,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
