import pygame

class Buttons():
    def __init__(self, width=150, height=50) -> None:
        self.width= width
        self.height = height
        self.button_surf = pygame.Surface((self.width, self.height))
        
    def button_get_rect(self):
        return self.button_surf.get_rect()

class ButtonImg(Buttons):
    def __init__(self,x,y,img,img_click=None,img_hover=None,alpha=False,width=150,height=50) -> None:
        super().__init__(width, height)
        self.button_img, self.button_surf = self.load_image(img, alpha)
        self.img_click = img_click
        self.img_hover = img_hover
        self.alpha = alpha
        self.x = x
        self.y = y
    
    def load_image(self, img, alpha):
        button_img_surf = pygame.imgae.load(img)
        if alpha:
            button_img = pygame.Surface.convert_alpha(button_img_surf)
        else:
            button_img = pygame.Surface.convert(button_img_surf)
        return button_img, button_img_surf
    
    def button_on_default(self, x=None, y=None):
        if x == None:
            x = self.x
        if y == None:
            y = self.y
        return (self.button_img,(x, y))
    
    def button_on_hover(self,x=None, y=None):
        if x == None:
            x = self.x
        if y == None:
            y = self.y
        if self.img_hover:
            img, surf = self.load_image(self.img_hover)
            return (img,(x, y))
        
    def button_on_click(self,x=None, y=None):
        if x == None:
            x = self.x
        if y == None:
            y = self.y
        if self.img_click:
            img, surf = self.load_image(self.img_click)
            return (img,(x, y))

class ButtonRect(Buttons):
    def __init__(self,x,y,color,color_click=None,color_hover=None,text=None,width=150,height=50) -> None:
        super().__init__(width, height)
        self.x = x
        self.y = y
        self.button_surf = pygame.Surface((self.x, self.y))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.button_click = color_click
        self.button_hover = color_hover
        self.color, self.color_click, self.color_hover = color, color_click, color_hover
        self.text = str(text)       
    
    def button_on_default(self, x=None, y=None):
        if x == None:
            x = self.x
        if y == None:
            y = self.y
        return (self.button_img,(x, y))
    
    def button_on_hover(self,x=None, y=None):
        if x == None:
            x = self.x
        if y == None:
            y = self.y
        if self.button_hover:
            return (self.button_hover,((x, y)(self.width, self.height)))
        
    def button_on_click(self,x=None, y=None):
        if x == None:
            x = self.x
        if y == None:
            y = self.y
        if self.button_click:
            return (self.button_hover,((x, y)(self.width, self.height)))
 