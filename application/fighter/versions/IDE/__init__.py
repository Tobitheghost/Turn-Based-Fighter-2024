from .game import IDE_GameLoop

def run(chr1, chr2):
    battle = IDE_GameLoop(chr1, chr2)
    while battle.still_alive() != False:
        battle.match_card()
        a, d, m, p = battle.show_moves()
        battle.attack_round(a, d, m, p)
        battle.rounds += 1
        battle.still_alive()

    print("\n\n" + battle.winner.name + " is the Winner!!\n\n")
