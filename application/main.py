from fighter.character import Player
from fighter.versions.IDE import run

Tobi = Player("Tobi", 100, 5, {"Tobi Moves":{"name":"Tobi Moves","move_type":"damage", "damage":95,"cost":100,"select_desc":"[-95 hp]","insuficient_cost": 0}}, accent_color="blue")
Cam = Player("Cam", 100, 5, {"Cam Moves":{"name":"Cam Moves","move_type":"damage", "damage":95,"cost":100,"select_desc":"[-95 hp]","insuficient_cost": 0}}, accent_color="red")

run(Tobi, Cam)