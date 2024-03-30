class Move():
    def __init__(self, name, description, hit_text, miss_text, invalid_move_text, elemnet, level):
        self.name = name
        self.description = description
        self.hit_text = hit_text
        self.miss_text = miss_text
        self.invalid_move_text = invalid_move_text
        self.elemnet = elemnet
        self.level = level

class DamageMove(Move):
    def __init__(self, name, description, hit_text, miss_text, invalid_move_text, move_type, elemnet, level, effect):
        super().__init__(name, description, hit_text, miss_text, invalid_move_text, elemnet, level)
        self.move_type = move_type
        self.effect = effect