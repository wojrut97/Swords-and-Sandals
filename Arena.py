import os
from os import system, name
import colorama

class Arena:
    def __init__(self):
        self.width = 30;
        self.arena = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',]

    def generate(self, player1_start_position, player2_start_position):
        self.arena[player1_start_position] = 'X'
        self.arena[player2_start_position] = 'O'

    def update_player_position(self, player_previous_position, player_position, player ):
        self.arena[player_previous_position] = '_'
        self.arena[player_position] = player

    def show(self, player1_position, player2_position):
        self.clear = lambda: os.system('clear')
        self.clear()
        for i in range(0, player1_position):
            print(colorama.Fore.WHITE + self.arena[i], end='')
        print(colorama.Fore.RED + self.arena[player1_position], end='')
        for i in range(player1_position+1, player2_position):
            print(colorama.Fore.WHITE + self.arena[i], end='')
        print(colorama.Fore.BLUE + self.arena[player2_position], end='')
        for i in range(player2_position+1, self.width):
            print(colorama.Fore.WHITE + self.arena[i], end='')

