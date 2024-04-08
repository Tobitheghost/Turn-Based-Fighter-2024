import pygame
import time

# Constants
# Display's
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Debug Display
debug_display = pygame.Surface((WIDTH // 7, HEIGHT // 2))
debug_pos = (2, 5)
# Font
FONT_NAME = pygame.font.get_default_font()
FONT_SIZE = 16
FONT = pygame.font.Font(FONT_NAME, FONT_SIZE)
# FPS
running_frames, running_seconds, fps = 0, 0, 0
previous_time = time.time()
# state
state_update = 0
update_dict = {"start": True}

def check_update():
    if update_dict["start"] == True:
        update_dict["main_menu_left_button_update"] = False
        update_dict["main_menu_right_button_update"] = False
    if "main_menu_left_button" in update_dict:
        update_dict["main_menu_left_button_update"] = update_dict[
            "main_menu_left_button"
        ].collidepoint(pygame.mouse.get_pos())
    if "main_menu_right_button" in update_dict:
        update_dict["main_menu_right_button_update"] = update_dict[
            "main_menu_right_button"
        ].collidepoint(pygame.mouse.get_pos())


def run(width, height, type):
    display = pygame.Surface((width, height))
    if type == "menu":
        pass  # only update on change
    if type == "game":
        pass  # update on new frame


def set_state(state="main_menu"):
    if state == "main_menu":
        run(main_menu)


def main_menu(width, height):
    display = pygame.Surface((width, height))
    display.fill("orange")

    # Title
    TITLE_FONT_SIZE = 30
    title_font = pygame.font.Font(FONT_NAME, TITLE_FONT_SIZE)
    title_surf = title_font.render("MAIN MENU", False, BLACK)
    title_rect = title_surf.get_rect()
    title_rect.center = width // 2, height // 2 - TITLE_FONT_SIZE
    display.blit(title_surf, title_rect)

    # Buttons
    button_size = (150, 50)
    button_offset = 10
    left_button = pygame.Rect((width // 2 - (button_size[0] + button_offset),height // 2 + button_size[1] // 4,),button_size,)
    right_button = pygame.Rect((width // 2 + button_offset, height // 2 + button_size[1] // 4), button_size)
    # Buttons Update
    update_dict["main_menu_left_button"] = left_button
    update_dict["main_menu_right_button"] = right_button
    # Buttons Colors
    lbtn_c = (150, 150, 0)
    rbtn_c = (0, 150, 150)

    if update_dict["main_menu_left_button_update"] == True:
        update_dict["main_menu_left_button_update"] = False
        update_dict["update_buffer"] = True
        lbtn_c = (255, 255, 0)
    if update_dict["main_menu_right_button_update"] == True:
        update_dict["main_menu_right_button_update"] = False
        update_dict["update_buffer"] = True
        rbtn_c = (0, 255, 255)

    # Buttons Updates
    pygame.draw.rect(display, lbtn_c, left_button)
    pygame.draw.rect(display, rbtn_c, right_button)
    return display

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.running = True
        self.font_name = pygame.font.get_default_font()
        self.font_size = FONT_SIZE
        self.title_size = TITLE_FONT_SIZE
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.debug_display = pygame.Surface((WIDTH // 7, HEIGHT // 2),SRCALPHA)
        self.debug_pos = (2, 5)
        self.debug = True
        self.running_frames = 0
        self.running_seconds = 0
        self.fps = 0
        self.previous_time = time.time()
        self.state_update = 0
        self.update_dict = {"start": True}
        self.black = (0,0,0)
    
    def debug_surf(self, surf, pos, fps, mouse_pos):
        debug_display.fill("orange")
        # FPS TEXT Section
        fps_text_surf = self.font.render("FPS:", False, self.white)
        fps_text_rect = fps_text_surf.get_rect()
        fps_text_rect = fps_text_rect.move(3, 10)
        surf.blit(fps_text_surf, fps_text_rect)
        # FPS Numbers
        numb_x = self.font_size * 2.5
        fps_numb_surf = self.font.render(str(fps), False, self.white)
        fps_numb_rect = fps_numb_surf.get_rect()
        fps_numb_rect = fps_numb_rect.move(fps_text_rect.x + numb_x, 10)
        surf.blit(fps_numb_surf, fps_numb_rect)
        # Mouse TEXT Position
        mouse_text_y = self.font_size * 1.5
        mouse_text_surf = self.font.render("Mouse:", False, self.white)
        mouse_text_rect = mouse_text_surf.get_rect()
        mouse_text_rect = mouse_text_rect.move(3, mouse_text_y + 10)
        surf.blit(mouse_text_surf, mouse_text_rect)
        # Mouse Position
        mouse_pos_surf = self.font.render(str(mouse_pos), False, self.white)
        mouse_pos_rect = mouse_pos_surf.get_rect()
        mouse_pos_rect = mouse_pos_rect.move(3, mouse_text_y + self.font_size + 10)
        surf.blit(mouse_pos_surf, mouse_pos_rect)
        return (surf,pos)
    
    def update_surfaces_to_screen(self, *surfaces):
        for surf in surfaces:
            self.screen.blit(surf)
    
    def update_loop(self):
        while self.running:
            
            #Get FPS and Delta Time
            delta_time = time.time() - self.previous_time
            self.previous_time = time.time()
            if self.running_seconds >= 1:
                self.fps = self.running_frames
                self.running_frames = 0
                self.running_seconds = 0
            else:
                self.running_seconds += delta_time
                self.running_frames += 1
            
            debug = self.debug_surf(self.debug_display,self.debug_pos, fps, pygame.mouse.get_pos())
            if self.debug == True:
                self.update_surfaces_to_screen(debug)

# Game Loop
running = True
while running:

    check_update()
    state_update = len([x for x in update_dict.values() if x == True])
    update_dict["update_buffer"] = False

    delta_time = time.time() - previous_time
    previous_time = time.time()
    if running_seconds >= 1:
        fps = running_frames
        running_frames = 0
        running_seconds = 0
    else:
        running_seconds += delta_time
        running_frames += 1

    if state_update:
        menu = main_menu(WIDTH, HEIGHT)
        screen.blit(menu, (0, 0))

    debug = debug_surf(debug_display, fps, pygame.mouse.get_pos())
    screen.blit(debug, debug_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            answer = pygame.display.message_box("Are you Leaving?",
                message="Are you sure you want to Quit the Game?",
                message_type="warn",
                buttons=("Yes", "Go Back"),
                escape_button=1)
            running = answer

    update_dict["start"] = False
    pygame.display.update()

pygame.quit()
