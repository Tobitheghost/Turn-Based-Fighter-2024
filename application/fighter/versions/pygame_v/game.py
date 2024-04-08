import pygame
from settings import *
from menu import MainMenu
import time

class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY, self.BACK_KEY, self.ESCAPE = False,False,False,False,False
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT, self.SCALE = WIDTH, HEIGHT, DISPLAY_ZOOM
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = BLACK, WHITE
        self.current_state = "X"
        self.current_menu = MainMenu(self, "Main Menu", 20, "Start","Options","Credits")
        self.previous_time = time.time() 
        self.debug_on = True
        self.running_seconds = 0
        self.running_frames = 0
        self.fps = 0
    
    def game_loop(self):
        while self.playing:
            self.display.fill(self.BLACK)
            self.check_events()
            if self.ENTER_KEY:
                self.playing = False
            self.draw_text("Thank you for Playing",20,self.DISPLAY_WIDTH//2, self.DISPLAY_HEIGHT//2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
    
    def debug(self, on, text):
        if on:
            self.draw_text(text, 20, 50, 50)
            self.draw_text(pygame.mouse.get_pos(), 20, 50, 100)

    def check_events(self):
        
        delta_time = time.time() - self.previous_time
        self.previous_time = time.time()
        if self.running_seconds >= 1:
            self.fps = self.running_frames
            self.running_frames = 0
            self.running_seconds = 0
        else:
            self.running_seconds += delta_time
            self.running_frames += 1
        self.debug(self.debug_on, f"FPS: {self.fps}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing, self.current_menu.run_display = False, False, False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = False
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = False
                if event.key == pygame.K_UP:
                    self.UP_KEY = False
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False
                        
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY, self.BACK_KEY = False,False,False,False
    
    def draw_text(self, text, size, x,y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(str(text), False, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
        return text_rect