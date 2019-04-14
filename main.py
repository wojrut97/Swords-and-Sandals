import Arena
import Player
import GameManager
import Stats
import Window

def main():
    arena = Arena.Arena()
    player1 = Player.Player('Wojtek', 11, Stats.hp, Stats.str, Stats.agi, 1, 'X')
    player2 = Player.Player('Seba',14, Stats.hp, Stats.str, Stats.agi, 0, 'O')
    arena.generate(player1.position, player2.position)
    now_playing = player1
    prev_playing = player2
    arena.show(player1.position, player2.position)
    Window.Window(arena, now_playing, prev_playing)



if __name__ == '__main__':
    main()