import pygame
import time
from settings import *
from builders.button import Button
from builders.menu import Menu
from menus.main_menu.buttons import start_btn, options_btn

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.FONT_NAME = pygame.font.get_default_font()
        self.FONT = pygame.font.Font(self.FONT_NAME, FONT_SIZE)
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running_frames = 0
        self.running_seconds = 0
        self.fps = 0
        self.previous_time = time.time()
        self.delta_time = time.time() - self.previous_time
        self.state_update = 1
        self.update_dict = {"start": True, "buttons":[]}
        self.main_menu = Menu(WIDTH, HEIGHT, "orange", "Main Menu",start_btn,options_btn)
        self.options_menu = Menu(WIDTH, HEIGHT, "blue", "Options",start_btn,options_btn)
        self.state = self.main_menu
        self.quit = False
    
    def update_state(self):
        self.state.add_to_mouse_update(self.update_dict)
    
    def check_update(self):
        for item in self.update_dict["buttons"]:
            if item.button.collidepoint(pygame.mouse.get_pos()):
                item.hover = True
                item.draw_button()
                if pygame.mouse.get_pressed()[0]:
                    item.click = True
                else:
                    if item.click == True:
                        item.draw_button()
                        if self.state == self.main_menu:
                            self.state = self.options_menu
                        else:
                            self.state = self.main_menu
                        item.click = False
            else:
                item.hover = False

    def quit_event(self):
        answer = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.quit == True:
                answer = pygame.display.message_box("Are you Leaving?",
                    message="Are you sure you want to Quit the Game?",
                    message_type="warn",
                    buttons=("Yes", "Go Back"),
                    escape_button=1)
        return answer

    def input_event(self):
        pass
    
    def end(self):
        pygame.quit()
    
    def get_fps(self):
        self.delta_time = time.time() - self.previous_time
        self.previous_time = time.time()
        if self.running_seconds >= 1:
            self.fps = self.running_frames
            self.running_frames = 0
            self.running_seconds = 0
        else:
            self.running_seconds += self.delta_time
            self.running_frames += 1
        
    def update(self):
        if self.update_dict["start"]:
            self.update_state()
            
        self.state.update(self.screen)
        self.check_update()
        self.get_fps()
        pygame.display.set_caption(str(self.fps))
        
        self.input_event()
        self.running = self.quit_event()
        
        self.update_dict["start"] = False
        pygame.display.update()
    
    def game_loop(self):
        while self.running:
            self.update()
            
        self.end()

game = Game()
game.game_loop()