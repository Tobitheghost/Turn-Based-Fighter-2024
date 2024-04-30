import pygame

pygame.font.init()

def create_text(text, font_size, font_name, font_color):
    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(text, False, font_color)
    text_rect = text_surface.get_rect()
    return text_surface, text_rect
