import pygame

class Menu():
    def __init__(self, game, width, height, background, title_text, title_size) -> None:
        self.width = width
        self.height = height
        self.background = background
        self.title_text = title_text
        self.title_size = title_size
        self.game = game
    
    def send_to_update(self,surface, *buttons, state):
        self.game.button_update_list(buttons, state)
        self.game.surface_update_list(surface, state)

class MainMenu(Menu):
    def __init__(self, game, background, button_menu_pair) -> None:
        Menu.__init__(game, self.game.width, self.game.height, background, "Main Menu", self.game.title_size)
        self.display_menu = pygame.Surface((self.width, self.height))
        self.background = background
        
        #Menu Title
        self.title_font = pygame.font.Font(self.game.font_name, self.title_size)
        self.title_surf = self.title_font.render(self.title_text, False, self.game.black)
        self.title_rect = self.title_surf.get_rect()
        self.title_rect.center = self.width//2,self.height//2-self.title_size
        self.display_menu.blit(self.title_surf, self.title_rect)
        
        #Menu Buttons