import pygame
from dataclasses import dataclass
from .create_text import create_text
from settings import *


@dataclass
class ProtoButton:
    name: str
    width: int
    height: int
    pos_x: int
    pos_y: int
    text: str
    primary_color: any = (1, 1, 1)
    hover_color: any = (151, 151, 151)

class Button:
    def __init__(
        self, name, width, height, pos_x, pos_y,text, primary_color, hover_color
    ) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.x = pos_x
        self.y = pos_y
        self.color1 = primary_color
        self.color2 = hover_color
        self.color3 = (
            max(primary_color[0] - 100, 0),
            max(primary_color[1] - 100, 0),
            max(primary_color[2] - 100, 0),
        )
        self.text_surf, self.text_rect = create_text(
            text, 16, pygame.font.get_default_font(), (20, 20, 20)
        )
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.btn_click = pygame.Rect(self.x, self.y + 5, self.width, self.height)
        self.btn_shadow = pygame.Rect(self.x, self.y + 5, self.width, self.height)
        self.hover = False
        self.click = False
        self.surface = None
        self.menu_call = None

    def draw_button(self, surface=None):
        if surface != None:
            if self.hover == True and self.click == False:
                pygame.draw.rect(surface, self.color3, self.btn_shadow, border_radius=12)
                pygame.draw.rect(surface, self.color2, self.button, border_radius=12)
                self.text_rect.center = self.button.center
                surface.blit(self.text_surf, self.text_rect)
            elif self.click:
                pygame.draw.rect(surface, self.color1, self.btn_click, border_radius=12)
                self.text_rect.center = self.btn_click.center
                surface.blit(self.text_surf, self.text_rect)
            else:
                pygame.draw.rect(surface, self.color3, self.btn_shadow, border_radius=12)
                pygame.draw.rect(surface, self.color1, self.button, border_radius=12)
                self.text_rect.center = self.button.center
                surface.blit(self.text_surf, self.text_rect)
        
    def switch_menu(self, state=None):
        if state != None:
            state.state_menu = self.menu_call
