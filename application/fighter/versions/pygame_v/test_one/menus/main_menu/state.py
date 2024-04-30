from dataclasses import asdict
from builders.state import StateMachine
from builders import button, menu
from .menu import _main_menu, _option_menu, _game_menu
from .buttons import (
    _start_btn,
    _options_btn,
    _opt_btn_1,
    _opt_btn_2,
    _opt_btn_3,
    _opt_btn_4,
    _opt_btn_5,
    _back_btn0,
    _back_btn1,
    _back_btn2,
)

# Game Instance
def init_state():
    
    init_main_btn0=button.Button(**asdict(_start_btn))
    init_main_btn1=button.Button(**asdict(_options_btn))
    init_main_btn2=button.Button(**asdict(_opt_btn_1))
    init_main_btn3=button.Button(**asdict(_opt_btn_2))
    init_main_btn4=button.Button(**asdict(_opt_btn_3))
    init_main_btn5=button.Button(**asdict(_opt_btn_4))
    init_main_btn6=button.Button(**asdict(_opt_btn_5))
    init_back_btn0=button.Button(**asdict(_back_btn0))
    init_back_btn1=button.Button(**asdict(_back_btn1))
    init_back_btn2=button.Button(**asdict(_back_btn2))
    
    
    temp_state = StateMachine(
    main_btn0=init_main_btn0,
    main_btn1=init_main_btn1,
    main_btn2=init_main_btn2,
    main_btn3=init_main_btn3,
    main_btn4=init_main_btn4,
    main_btn5=init_main_btn5,
    main_btn6=init_main_btn6,
    back_btn0=init_back_btn0,
    back_btn1=init_back_btn1,
    back_btn2=init_back_btn2)
    
    temp_state.main_menu = menu.Menu(
    temp_state.main_btn0, temp_state.main_btn1, **asdict(_main_menu))
    
    temp_state.sub_menu1 = menu.Menu(
    temp_state.back_btn0,
    **asdict(_game_menu))
    
    temp_state.sub_menu2 = menu.Menu(
    temp_state.main_btn2,
    temp_state.main_btn3,
    temp_state.main_btn4,
    temp_state.main_btn5,
    temp_state.main_btn6,
    **asdict(_option_menu))
    
    # Main Menu Buttons Init (setting blit surface, what menu called on click)
    temp_state.main_menu.set_button_surf()
    temp_state.init_buttons()
    temp_state.set_menu_call(temp_state.main_btn0, temp_state.sub_menu1)
    temp_state.set_menu_call(temp_state.main_btn1, temp_state.sub_menu2)
    temp_state.set_menu_call(temp_state.back_btn0, print("Close Pygame"))
    # Game Instance Buttons Init (setting blit surface, what menu called on click)
    temp_state.sub_menu1.set_button_surf()
    temp_state.init_buttons()
    temp_state.set_menu_call(temp_state.back_btn1, temp_state.main_menu)
    # Option Menu Buttons Init (setting blit surface, what menu called on click)
    temp_state.sub_menu2.set_button_surf()
    temp_state.init_buttons()
    temp_state.set_menu_call(temp_state.main_btn2, temp_state.sub_menu1)
    temp_state.set_menu_call(temp_state.main_btn3, temp_state.sub_menu2)
    temp_state.set_menu_call(temp_state.main_btn4, temp_state.sub_menu1)
    temp_state.set_menu_call(temp_state.main_btn5, temp_state.sub_menu2)
    temp_state.set_menu_call(temp_state.main_btn6, temp_state.sub_menu1)
    temp_state.set_menu_call(temp_state.back_btn2, temp_state.main_menu)
    
    return temp_state

game_main_menu = init_state()