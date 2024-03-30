class Player():
    def __init__(self, name, max_hp, strength, moves:dict, accent_color:str ='white'):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.strength = strength
        moves.update({"punch":{"name":"punch","move_type":"damage", "damage":5,"cost":10,"select_desc":"[-5 hp]","insuficient_cost": 2},
                    "covid": {"name":"covid","move_type":"status","status":"poison","cost":15,"select_desc":None,"insuficient_cost": 0},
                    "heal": {"name":"heal","move_type":"heal","heal":5,"cost":20,"select_desc":"[+5 hp]","insuficient_cost": 0}})
        self.moves = moves
        self.alive = True
        self.color = accent_color
        self.status = []

    def get_moves(self):
        move_list = []
        itter_moves = self.moves.keys()
        for move in itter_moves:
            move_list.append((move))
        return move_list