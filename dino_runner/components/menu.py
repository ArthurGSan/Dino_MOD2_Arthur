import pygame
import os

from pygame.locals import *
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.utils.constants import YELLOW, JUMPING, SCREEN_HEIGHT, SCREEN_WIDTH, IMG_DIR

MENU_IMG = JUMPING
HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

DINO_IMG = JUMPING

FONT_SIZE = 40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACK_GROUND = pygame.image.load(os.path.join(IMG_DIR, 'Other/Background-night.png')).convert()
BACK_GROUND = pygame.transform.scale(BACK_GROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))


class Menu:
    def __init__(self):
        self.options = ["start", "shop", "credits", "exit"]
        self.index = 0
        self.shop_index = 0
        self.shop_menu = False
        self.rank_menu = False

    def select(self):
        return self.options[self.index].lower()

    def change_selection(self, dir, index, list):
        index += dir
        if index >= len(list):
            index = 0
        elif index < 0:
            index = len(list) - 1
        return index

    def check_index(self, index):
        if self.index == index:
            return YELLOW
        else:
            return (0, 0, 0)
        
    def game_quit(self, game):
        game.playing = False
        game.running = False

    def exec_esc(self, game):
        if self.shop_menu:
            self.shop_menu = False
        elif self.rank_menu:
            self.rank_menu = False
        else:
            self.game_quit(game)
    
    def show_menu(self, game, screen, score, death_count, all_time_score, rank_menu):
        if not self.shop_menu and not self.rank_menu:
            self.draw_menu(screen, score, death_count)
            self.handle_events_on_menu(game)
        elif self.shop_menu:
            self.draw_shop_menu(screen, all_time_score)
            self.handle_events_on_shop_menu(game)
        elif self.rank_menu:
            self.draw_rank_menu(screen, rank_menu)
            self.handle_events_on_rank_menu(game)

    def handle_events_on_rank_menu(self, game):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exec_esc(game)
            if event.type == QUIT:
                game.playing = False
                game.running = False

    def handle_events_on_shop_menu(self, game):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if [K_SPACE, K_KP_ENTER, K_RETURN].__contains__(event.key):
                    option_selected = self.select()
                elif event.key == K_ESCAPE:
                    self.exec_esc(game)
                elif event.key == K_LEFT or event.key == K_a:
                    self.shop_index = self.change_selection(-1, self.shop_index, self.shop_options)
                elif event.key == K_RIGHT or event.key == K_d:
                    self.shop_index = self.change_selection(1, self.shop_index, self.shop_options)
            elif event.type == QUIT:
                game.playing = False
                game.running = False

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if [K_SPACE, K_KP_ENTER, K_RETURN].__contains__(event.key):
                    option_selected = self.select()
                    if ["start", "restart"].__contains__(option_selected):
                        game.run()
                    elif option_selected == "shop":
                        self.shop_menu = True
                    elif option_selected == "exit":
                        self.game_quit(game)
                    elif option_selected == "rank":
                        self.rank_menu = True
                    elif option_selected == "credits":
                        option_selected == True
                elif event.key == K_ESCAPE:
                    self.exec_esc(game)
                elif event.key == K_UP or event.key == K_w:
                    self.index = self.change_selection(-1, self.index, self.options)
                elif event.key == K_DOWN or event.key == K_s:
                    self.index = self.change_selection(1, self.index, self.options)
            elif event.type == QUIT:
                game.playing = False
                game.running = False

    def draw_shop_menu(self, screen, all_time_score):
        screen.fill((255, 255, 255))
        draw_message_component(
                f"Shop points: {all_time_score}",
                screen,
                pos_x_center = 1000,
                pos_y_center = 50
            )
        pygame.display.flip()

    def draw_rank_menu(self, screen, rank_menu):
        # screen.fill((255, 255, 255))
        screen.blit(BACK_GROUND, (0, 0))   
        height = screen.get_height()
        draw_message_component(
                "Rank",
                screen,
                font_size = FONT_SIZE, 
                pos_y_center = 50
            )
        for index, option in enumerate(rank_menu):
            draw_message_component(
                f"{index + 1}. {option}",
                screen,
                font_size = FONT_SIZE,
                pos_y_center = FONT_SIZE + height / 3 + (FONT_SIZE * 2 * index)
            )
        pygame.display.flip()

    def draw_menu(self, screen, score, death_count):
        screen.fill((255, 255, 255))
        height = screen.get_height()
        if death_count == 0:
            self.options = ["start", "shop", "credits", "exit"]
        else: 
            self.options = ["restart", "shop", "credits", "rank", "exit"]
            draw_message_component(
                f"Last score: {score}",
                screen,
                pos_x_center = HALF_SCREEN_WIDTH - HALF_SCREEN_WIDTH / 2
            )
            draw_message_component(
                f"Death count: {death_count}",
                screen,
                pos_x_center = HALF_SCREEN_WIDTH + HALF_SCREEN_WIDTH / 2
            )

        menu_img_width = MENU_IMG.get_width()
        menu_img_height = MENU_IMG.get_height()
        scaled_mult = 2
        menu_img_scaled = pygame.transform.scale(MENU_IMG, (menu_img_width * scaled_mult, menu_img_height * scaled_mult))
        screen.blit(menu_img_scaled, (10 + HALF_SCREEN_WIDTH - menu_img_scaled.get_width() / 2, HALF_SCREEN_HEIGHT - FONT_SIZE * 4 - MENU_IMG.get_height()))

        for index, option in enumerate(self.options):
            draw_message_component(
                f"{option.capitalize()}",
                screen,
                font_color = self.check_index(index),
                font_size = FONT_SIZE,
                pos_y_center = FONT_SIZE * 3 + height / 3 + (FONT_SIZE * 2 * index)
            )
        pygame.display.flip()