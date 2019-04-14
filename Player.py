import Arena
import math
import GameManager

class Player:
    def __init__(self, name, start_position, hp, str, agi, direction, symbol):
        self.name = name
        self.position = start_position
        self.hp = hp
        self.str = str
        self.agi = agi
        self.direction = direction
        self.symbol = symbol

    def step_forward(self, arena):
        previous_position = self.position
        if self.direction:
            self.position += self.agi

        else:
            self.position -= self.agi
        actual_position = self.position
        arena.update_player_position(previous_position, actual_position, self.symbol)

    def step_backward(self, arena):
        previous_position = self.position
        if self.direction:
            self.position -= self.agi

        else:
            self.position += self.agi
        actual_position = self.position
        arena.update_player_position(previous_position, actual_position, self.symbol)

    def quick_attack(self, enemy):
        if math.fabs(enemy.position - self.position) <= 1:
            if GameManager.GameManager.get_random('quick'):
                enemy.hp -= self.str
            else:
                print('miss')

    def normal_attack(self, enemy):
        if math.fabs(enemy.position - self.position) <= 1:
            if GameManager.GameManager.get_random('quick'):
                enemy.hp -= self.str*2
            else:
                print('miss')

    def power_attack(self, enemy):
        if math.fabs(enemy.position - self.position) <= 1:
            if GameManager.GameManager.get_random('quick'):
                enemy.hp -= self.str*4
            else:
                print('miss')