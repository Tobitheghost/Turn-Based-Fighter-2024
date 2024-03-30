class HealthBar:
    EMPTY_BLOCKS = "▯"
    FULL_BLOCKS = "▮"
    color_options = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "orange": "\033[33m",
        "blue": "\033[34m",
        "purple": "\033[35m",
        "cyan": "\033[36m",
        "lightgrey": "\033[37m",
        "darkgrey": "\033[90m",
        "lightred": "\033[91m",
        "lightgreen": "\033[92m",
        "yellow": "\033[93m",
        "lightblue": "\033[94m",
        "pink": "\033[95m",
        "lightcyan": "\033[96m",
        "white": "\033[0m",
    }

    def __init__(self, player, pos_numb, color: str = "white") -> None:
        self.player = player
        self.pos_numb = pos_numb
        if color in self.color_options.keys():
            self.color = self.color_options[color]
        else:
            raise ValueError(
                f"{color} isnt a valid Color option. The Options are:\n{self.color_options.keys()}"
            )

    def health_bars(self):
        full_hp_bars_numb = self.player.max_hp // 10
        remaining_hp_bars_numb = (self.player.hp) // 10
        empty_hp_bars_numb = full_hp_bars_numb - remaining_hp_bars_numb

        if 0 < self.player.hp / 10 < 1:
            remaining_hp_bars_numb = 1
            empty_hp_bars_numb -= 1

        remaining_hp_bars = remaining_hp_bars_numb * self.FULL_BLOCKS
        empty_hp_bars = empty_hp_bars_numb * self.EMPTY_BLOCKS

        return [
            f"[{self.color}{remaining_hp_bars}{self.color_options['white']}{empty_hp_bars} ]",
            f"[{remaining_hp_bars}{empty_hp_bars} ]",
        ]

    def match_card_text(self):

        p_name_card = f"Player {self.pos_numb}: {self.player.name}"

        p_health_card = f"Health: {self.player.hp}/{self.player.max_hp}"

        p_hp_bar_card = self.health_bars()

        return p_name_card, p_health_card, p_hp_bar_card
