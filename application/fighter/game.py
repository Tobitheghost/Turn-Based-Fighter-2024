class GameLoop:

    def __init__(self, combatant1, combatant2):
        self.combatant1 = combatant1
        self.combatant2 = combatant2
        self.winner = None
        self.rounds = 0
        self.turn = 1

    def still_alive(self):
        if self.combatant1.hp < 1:
            self.combatant1.alive = False
            self.winner = self.combatant2
            return False
        if self.combatant2.hp < 1:
            self.combatant2.alive = False
            self.winner = self.combatant1
            return False

    def attack_effect(self):
        pass

    def attack_round(self, attacker, defender, move_name, player):
        if attacker.moves[move_name]["move_type"] == "damage":
            effect = attacker.moves[move_name]["damage"]
            defender.hp -= effect
            pass
        elif attacker.moves[move_name]["move_type"] == "status":
            effect = attacker.moves[move_name]["status"]
            defender.status.append(effect)
            pass
        elif attacker.moves[move_name]["move_type"] == "heal":
            effect = attacker.moves[move_name]["heal"]
            if attacker.hp + effect > attacker.max_hp:
                attacker.hp = attacker.max_hp
            else:
                attacker.hp += effect
            pass
        else:
            raise ValueError(f"{move_name} doesnt Seem to be a Valid Move\n")

        self.turn = player
