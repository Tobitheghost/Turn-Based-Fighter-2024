import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_width, self.mid_height = self.game.DISPLAY_WIDTH//2, self.game.DISPLAY_HEIGHT//2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
        
    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor_rect.x, self.cursor_rect.y)
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()
            
class MainMenu(Menu):
    def __init__(self, game, current_menu_name, name_gap, *submenu_names):
        Menu.__init__(self, game)
        self.menu_name = current_menu_name # "Main Menu"
        self.gap = name_gap # 20 || gab between Sub Menu Headings
        self.menu_dict = {} # Start, Options, Credits
        self.submenus = list(submenu_names)
        for count, submenus in enumerate(self.submenus):
            sub = {"name":submenus,"x":self.mid_width, "y":self.mid_height+((count+1) * self.gap)}
            self.menu_dict[submenus] = sub
        self.state = self.submenus[0] # Start Game
        self.cursor_rect.midtop = (self.menu_dict[self.state]["x"] + self.offset, self.menu_dict[self.state]["y"])
        self.menu_rects = []
        self.start_mouse = False
        
    def check_mouse(self, pos):
        if pygame.mouse.get_focused():
            for submenu in self.submenus:
                if c_rect.collidepoint(pos):
                    self.cursor_rect.midtop = (self.menu_dict[self.submenus[self.menu_rects.index(c_rect)]]['x'] + self.offset, self.menu_dict[self.submenus[self.menu_rects.index(c_rect)]]['y'])
                    self.state = self.submenus[self.menu_rects.index(c_rect)]
                    self.game.draw_text("Hover", 20, 50, 200)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill(self.game.BLACK)
            self.game.check_events()
            self.check_input()
            self.game.draw_text(self.menu_name, 20, self.mid_width, self.mid_height - self.gap)
            for submenu in self.submenus:
                smenu = self.menu_dict[submenu]
                self.menu_rects.append(self.game.draw_text(smenu["name"], 20, smenu["x"], smenu["y"]))
            self.check_mouse(pygame.mouse.get_pos())
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.game.DOWN_KEY:
            next = 0
            while self.state != self.submenus[next - 1]:
                next += 1
                if next > len(self.submenus):
                    next = 0
            self.cursor_rect.midtop = (self.menu_dict[self.submenus[next]]['x'] + self.offset, self.menu_dict[self.submenus[next]]['y'])
            self.state = self.submenus[next]
        if self.game.UP_KEY:
            next = -1
            while self.state != self.submenus[next + 1]:
                next += 1
                if next > len(self.submenus):
                    next = -1
            self.cursor_rect.midtop = (self.menu_dict[self.submenus[next]]['x'] + self.offset, self.menu_dict[self.submenus[next]]['y'])
            self.state = self.submenus[next]

    def check_input(self):
        self.move_cursor()
        if self.game.ENTER_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                pass
            elif self.state == "Credits":
                pass
            self.run_display = False