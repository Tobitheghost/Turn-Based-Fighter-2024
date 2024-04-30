import pygame
from .button import Button
from dataclasses import dataclass
from settings import *

@dataclass
class ProtoMenu:
    width:int
    height:int
    fill: tuple
    title: str
    
class Menu():
    def __init__(self,*buttons, width, height, fill, title) -> None:
        self.width = width
        self.height = height
        self.fill = fill
        
        #Menu Display
        self.surf = pygame.Surface((self.width, self.height))
        
        #Title
        self.title_text = title
        self.font_size = 30
        self.font_name = pygame.font.get_default_font()
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.font_color = (1,1,1)
        self.title_surf = self.font.render(self.title_text, False, self.font_color)
        self.title_rect = self.title_surf.get_rect(center = (self.width//2, self.height//2 - self.font_size))
        
        #Buttons
        self.buttons = buttons
        
    def set_button_surf(self):
        for button in self.buttons:
            button.surface = self.surf
    
    def draw_background(self):
        self.surf.fill(self.fill)
        self.surf.blit(self.title_surf, self.title_rect)
        
    def draw_buttons(self):
        for button in self.buttons:
            button.draw_button(self.surf)
        
    def update(self, screen):
        self.draw_background()
        self.draw_buttons()
        screen.blit(self.surf, (0,0))
                    
