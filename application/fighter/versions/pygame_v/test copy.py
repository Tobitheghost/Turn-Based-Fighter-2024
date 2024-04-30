import pygame
import time

pygame.init()
running = True
# Constants
WIDTH, HEIGHT, WHITE, BLACK = 640, 360, (255, 255, 255), (0, 0, 0)
# Display's
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Debug Display
debug_display = pygame.Surface((WIDTH // 7, HEIGHT // 2),pygame.SRCALPHA)
debug_pos = (2, 5)

# Font
FONT_NAME = pygame.font.get_default_font()
FONT_SIZE = 16
FONT = pygame.font.Font(FONT_NAME, FONT_SIZE)
# FPS
running_frames, running_seconds, fps = 0, 0, 0
previous_time = time.time()
# state
state_update = 1
update_dict = {"start": True, "buttons":[]}


def debug_surf(surf, fps, mouse_pos):
    debug_display.fill(("orange"))
    # FPS TEXT Section
    fps_text_surf = FONT.render("FPS:", False, WHITE)
    fps_text_rect = fps_text_surf.get_rect()
    fps_text_rect = fps_text_rect.move(3, 10)
    surf.blit(fps_text_surf, fps_text_rect)
    # FPS Numbers
    numb_x = FONT_SIZE * 2.5
    fps_numb_surf = FONT.render(str(fps), False, WHITE)
    fps_numb_rect = fps_numb_surf.get_rect()
    fps_numb_rect = fps_numb_rect.move(fps_text_rect.x + numb_x, 10)
    surf.blit(fps_numb_surf, fps_numb_rect)
    # Mouse TEXT Position
    mouse_text_y = FONT_SIZE * 1.5
    mouse_text_surf = FONT.render("Mouse:", False, WHITE)
    mouse_text_rect = mouse_text_surf.get_rect()
    mouse_text_rect = mouse_text_rect.move(3, mouse_text_y + 10)
    surf.blit(mouse_text_surf, mouse_text_rect)
    # Mouse Position
    mouse_pos_surf = FONT.render(str(mouse_pos), False, WHITE)
    mouse_pos_rect = mouse_pos_surf.get_rect()
    mouse_pos_rect = mouse_pos_rect.move(3, mouse_text_y + FONT_SIZE + 10)
    surf.blit(mouse_pos_surf, mouse_pos_rect)
    return surf

def check_update():
    for item in update_dict["buttons"]:
        item.hover = item.button.collidepoint(pygame.mouse.get_pos())
        item.draw_button()

class Menu():
    def __init__(self, width, height, fill, title) -> None:
        self.width = width
        self.height = height
        self.fill = fill
        self.menu_init = False
        
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
        self.button_width = 150
        self.button_height = 50
        self.button_offset = 10
        self.lb_pos_x = self.width // 2 - (self.button_width + self.button_offset)
        self.lb_pos_y = self.height // 2 - self.button_height // 8
        self.rb_pos_x = self.width // 2 + self.button_offset
        self.rb_pos_y = self.height // 2 - self.button_height // 8
        self.left_button = Button(self.button_width, self.button_height, self.lb_pos_x,self.lb_pos_y,(150, 150, 0),(255, 255, 0))
        self.left_button.surface = self.surf
        self.right_button = Button(self.button_width, self.button_height, self.rb_pos_x,self.rb_pos_y,(0, 150, 150),(0, 255, 255))
        self.right_button.surface = self.surf
        self.button_init = False
        
    def create_title(self):
        self.text_surf = self.font.render(self.title_text, False, self.font_color)
        self.text_rect = self.text_surf.get_rect(center = (self.width//2, self.height//2 - self.font_size))
    
    def create_buttons(self):
        self.left_button = Button(self.button_width, self.button_height, self.lb_pos_x,self.lb_pos_y,(150, 150, 0),(255, 255, 0))
        self.right_button = Button(self.button_width, self.button_height, self.rb_pos_x,self.rb_pos_y,(0, 150, 150),(0, 255, 255))
    
    def update(self, screen):
        if self.menu_init == False:
            self.surf.fill(self.fill)
            self.surf.blit(self.title_surf, self.title_rect)
            self.menu_init = True
        self.left_button.draw_button(self.surf)
        self.right_button.draw_button(self.surf)
        screen.blit(self.surf, (0,0))
    
    def add_to_mouse_update(self):
        if self.button_init == False:
            if self.left_button and self.right_button in update_dict["buttons"]:
                self.button_init = True
            else:
                update_dict["buttons"].append(self.left_button)
                update_dict["buttons"].append(self.right_button)
                self.button_init = True

def quit_event():
    answer = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            answer = pygame.display.message_box("Are you Leaving?",
                message="Are you sure you want to Quit the Game?",
                message_type="warn",
                buttons=("Yes", "Go Back"),
                escape_button=1)
    return answer
    
# Game Loop

mainmenu = Menu(WIDTH, HEIGHT, "orange", "Main Menu")
while running:

    check_update()

    delta_time = time.time() - previous_time
    previous_time = time.time()
    if running_seconds >= 1:
        fps = running_frames
        running_frames = 0
        running_seconds = 0
    else:
        running_seconds += delta_time
        running_frames += 1
        
    mainmenu.update(screen)
    if state_update:
        mainmenu.update(screen)
        mainmenu.add_to_mouse_update()

    pygame.display.set_caption(str(fps))
    # debug = debug_surf(debug_display, fps, pygame.mouse.get_pos())
    # screen.blit(debug, debug_pos)

    running = quit_event()

    update_dict["start"] = False
    pygame.display.update()

pygame.quit()
