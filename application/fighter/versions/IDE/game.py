from .health_bar import HealthBar
from fighter.game import GameLoop

class IDE_GameLoop(GameLoop):
    border = {
        "top_left": "┏",
        "top_right": "┓",
        "bottom_left": "┗",
        "bottom_right": "┛",
        "vertical": "┃",
        "horizontal": "━",
    }

    def __init__(self, combatant1, combatant2):
        super().__init__(combatant1, combatant2)

    def match_card_gen(self, card_width: int = 120, padding_numb: int = 2):
        spacer = " "
        padding = padding_numb * spacer

        p1_health = HealthBar(self.combatant1, "1", self.combatant1.color)
        p2_health = HealthBar(self.combatant2, "2", self.combatant2.color)

        pos1_1, pos2_1, pos3_1 = p1_health.match_card_text()
        pos1_2, pos2_2, pos3_2 = p2_health.match_card_text()

        pos1_gap = (card_width - (padding_numb * 2)) - (len(pos1_1) + len(pos1_2))
        pos2_gap = (card_width - (padding_numb * 2)) - (len(pos2_1) + len(pos2_2))
        pos3_gap = (card_width - (padding_numb * 2)) - (len(pos3_1[1]) + len(pos3_2[1]))

        pos1 = f"{padding}{pos1_1}{pos1_gap*spacer}{pos1_2}{padding}"
        pos2 = f"{padding}{pos2_1}{pos2_gap*spacer}{pos2_2}{padding}"
        pos3 = f"{padding}{pos3_1[0]}{pos3_gap*spacer}{pos3_2[0]}{padding}"

        return pos1, pos2, pos3, card_width

    def match_card(self):
        pos1, pos2, pos3, card_width = self.match_card_gen()

        pos_top = f"{self.border['top_left']}{self.border['horizontal']*(card_width)}{self.border['top_right']}"
        pos_bottom = f"{self.border['bottom_left']}{self.border['horizontal']*(card_width)}{self.border['bottom_right']}"
        pos_middle = f"{self.border['vertical']}{pos1}{self.border['vertical']}\n{self.border['vertical']}{pos2}{self.border['vertical']}\n{self.border['vertical']}{pos3}{self.border['vertical']}"

        print(f"{pos_top}\n{pos_middle}\n{pos_bottom}")

    def show_moves(self):
        if self.turn == 1:
            attacker = self.combatant1
            defender = self.combatant2
            player = 2
        if self.turn == 2:
            attacker = self.combatant2
            defender = self.combatant1
            player = 1
        moves = attacker.get_moves()
        move_name = ""
        print(f"{attacker.name} pick a Move (Enter Number):")
        valid_choices = []
        for numb, move in enumerate(moves):
            print(f'{numb}). {move} {str(attacker.moves[move]["select_desc"])}')
            valid_choices.append(str(numb))
        is_valid = False
        while is_valid == False:
            choice = input()
            if choice in valid_choices:
                is_valid = True
            else:
                print(f"'{choice}' isnt a valid choice. Enter a number")
        move_name = moves[int(choice)]
        print(move_name)
        return attacker, defender, move_name, player