import pygame
class StateMachine:
    def __init__(self, 
                main_menu = None, 
                sub_menu1 = None, 
                sub_menu2 = None,
                main_btn0 = None,
                main_btn1 = None,
                main_btn2 = None,
                main_btn3 = None,
                main_btn4 = None,
                main_btn5 = None,
                main_btn6 = None,
                main_btn7 = None,
                main_btn8 = None,
                main_btn9 = None,
                back_btn0 = None,
                back_btn1 = None,
                back_btn2 = None,
                ) -> None:
        
        # Game Instance
        self.game = None
        # Main Menu
        self.main_menu = main_menu
        ## Sub-Menus
        self.sub_menu1 = sub_menu1
        self.sub_menu2 = sub_menu2

        # Main Menu buttons
        self.button_init = False
        self.main_btn0 = main_btn0
        self.main_btn1 = main_btn1
        self.main_btn2 = main_btn2
        self.main_btn3 = main_btn3
        self.main_btn4 = main_btn4
        self.main_btn5 = main_btn5
        self.main_btn6 = main_btn6
        self.main_btn7 = main_btn7
        self.main_btn8 = main_btn8
        self.main_btn9 = main_btn9
        self.back_btn0 = back_btn0
        self.back_btn1 = back_btn1
        self.back_btn2 = back_btn2
        self.button_list = list()

        # State
        self.menu_state = self.main_menu
        self.update_dict = {"start": True, "buttons": []}
        self.menu_update = {"menu_state":None,"button_state":[]}

    ## Menu State Machine
    def init_buttons(self):
        btn_list = [
            self.main_btn0,
            self.main_btn1,
            self.main_btn2,
            self.main_btn3,
            self.main_btn4,
            self.main_btn5,
            self.main_btn6,
            self.main_btn7,
            self.main_btn8,
            self.main_btn9,
        ]
        self.update_dict["buttons"] = self.button_list = [
            button for button in btn_list if button != False]
    
    def set_menu_call(self, state_button, state_menu):
        state_button.menu_call = state_menu
    
    def init_state(self, screen):
        if self.menu_state != None:
            self.menu_state.update(screen)
        else:
            self.menu_state = self.main_menu
        self.init_buttons()
        
    def update(self):
        if self.menu_state != None:
            for button in self.menu_state.buttons:
                if button.button.collidepoint(pygame.mouse.get_pos()):
                    button.hover = True
                    self.menu_state.draw_buttons()
                    if pygame.mouse.get_pressed()[0]:
                        button.click = True
                    else:
                        if button.click == True:
                            self.menu_state.draw_buttons()
                            button.menu_call()
                            button.click = False
                else:
                    button.hover = False

    def state_update(self):
        # Main Menu States
        if self.menu_state == self.main_menu:
            if self.main_btn1.click == True:
                self.menu_state = self.sub_menu1
            if self.main_btn2.click == True:
                self.menu_state = self.sub_menu2
            if self.back_button.click == True:
                self.game.quit = True
        # Sub Menu1 States
        if self.menu_state == self.sub_menu1:
            if self.back_button.click == True:
                self.menu_state = self.main_menu
        # Sub Menu2 States
        if self.menu_state == self.sub_menu2:
            if self.back_button.click == True:
                self.menu_state = self.main_menu
