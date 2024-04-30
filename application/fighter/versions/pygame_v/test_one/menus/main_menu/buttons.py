from builders import button
from settings import *

_start_btn = button.ProtoButton(
    "m_main_start_btn",
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    MM_L_BUTTON_X,
    MM_BUTTON_Y,
    "Start Game",
    (150, 150, 0),
    (255, 255, 0),
)
_options_btn = button.ProtoButton(
    "m_main_options_btn",
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    MM_R_BUTTON_X,
    MM_BUTTON_Y,
    "Options",
    (0, 150, 150),
    (0, 255, 255),
)
_opt_btn_1 = button.ProtoButton(
    "m_option_btn_one",
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    QTR_WIDTH,
    BUTTON_WIDTH + BUTTON_OFFSET + (TITLE_SIZE * 1),
    "Option One",
    (0, 150, 150),
    (0, 255, 255),
)
_opt_btn_2 = button.ProtoButton(
    "m_option_btn_two",
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    QTR_WIDTH,
    BUTTON_WIDTH + BUTTON_OFFSET + (TITLE_SIZE * 2),
    "Option Two",
    (0, 150, 150),
    (0, 255, 255),
)
_opt_btn_3 = button.ProtoButton(
    "m_option_btn_three",
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    QTR_WIDTH,
    BUTTON_WIDTH + BUTTON_OFFSET + (TITLE_SIZE * 3),
    "Option Three",
    (0, 150, 150),
    (0, 255, 255),
)
_opt_btn_4 = button.ProtoButton(
    "m_option_btn_four",
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    QTR_WIDTH,
    BUTTON_WIDTH + BUTTON_OFFSET + (TITLE_SIZE * 4),
    "Option Four",
    (0, 150, 150),
    (0, 255, 255),
)
_opt_btn_5 = button.ProtoButton(
    "m_option_btn_five",
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    QTR_WIDTH,
    BUTTON_WIDTH + BUTTON_OFFSET + (TITLE_SIZE * 5),
    "Option Five",
    (0, 150, 150),
    (0, 255, 255),
)
_back_btn0 = button.ProtoButton(
    "back_button_one",
    BUTTON_WIDTH,
    BUTTON_WIDTH,
    WIDTH + 20,
    20,
    "X",
    (180, 200, 200),
    (200, 220, 220),
)
_back_btn1 = button.ProtoButton(
    "back_button_two",
    BUTTON_WIDTH,
    BUTTON_WIDTH,
    WIDTH + 20,
    20,
    "X",
    (180, 200, 200),
    (200, 220, 220),
)
_back_btn2 = button.ProtoButton(
    "back_button_three",
    BUTTON_WIDTH,
    BUTTON_WIDTH,
    WIDTH + 20,
    20,
    "<|",
    (180, 200, 200),
    (200, 220, 220),
)