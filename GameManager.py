import random

class GameManager:
    def __init__(self, quit):
        self.quit = quit

    def player_action(self, player, arena, enemy):                                              #not used since window is implemented (for console gaming only)
        for i in range(3):
            print(" ")
            print("Wybierz akcje, " + player.name + ": ")
            print("1. Krok naprzod")
            print("2. Krok w tyl")
            print("3. Szybki cios")
            print("4. Sredni cios")
            print("5. Silny cios")
            player_input = input()
            if player_input == '1':
                player.step_forward(arena)
                break;
            elif player_input == '2':
                player.step_backward(arena)
                break;
            elif player_input == '3':
                player.quick_attack(enemy)
                break;
            elif player_input == '9':
                self.quit = 1
                break;
            else:
                print("Nie pogrywaj ze mna koleszko")

    @staticmethod
    def change_player(prev, next):
        return next, prev

    @staticmethod
    def get_random(attack):                                                         #generates a random chance for an attack
        quick_chance = 80
        normal_chance = 60
        power_chance = 40
        rand = random.randint(1, 100)
        if attack == 'quick':
            if(rand < quick_chance):
                return 1
            else:
                return 0

        if attack == 'normal':
            if(rand < normal_chance):
                return 1
            else:
                return 0

        if attack == 'power':
            if(rand < power_chance):
                return 1
            else:
                return 0
        else:
            print("cos sie zepsulo")
            return 0

    @staticmethod
    def is_dead(player1, player2):                                                                  #checks if any player is dead
        if (player1.hp <= 0):
            return player1.name
        if (player2.hp <= 0):
            return player2.name
        return False
