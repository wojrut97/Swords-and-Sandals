from PyQt5 import QtWidgets
import GameManager


class Window:

    def __init__(self, arena, prev_player, now_player):
        self.prev_player = prev_player
        self.now_player = now_player
        self.arena = arena
        self.app = QtWidgets.QApplication([])
        self.w = QtWidgets.QWidget()
        self.w.setWindowTitle('Miecze i Sandały')
        self.w.setGeometry(100, 100, 600, 400)
        self.main_label()
        self.player1_hp_label()
        self.player2_hp_label()
        self.who_plays_label()
        self.quit_button()
        self.start_button()
        self.forward_button()
        self.backward_button()
        self.quick_attack_button()
        self.normal_attack_button()
        self.power_attack_button()
        self.w.show()
        self.app.exec_()

    def main_label(self):
        self.label = QtWidgets.QLabel(self.w)
        self.label.move(100, 100)
        self.label.setText(''.join(self.arena.arena))

    def player1_hp_label(self):
        self.hp_label1 = QtWidgets.QLabel(self.w)
        self.hp_label1.move(500, 100)
        self.hp_label1.setText(str(self.now_player.hp))

    def player2_hp_label(self):
        self.hp_label2 = QtWidgets.QLabel(self.w)
        self.hp_label2.move(520, 100)
        self.hp_label2.setText(str(self.prev_player.hp))

    def who_plays_label(self):
        self.player_label = QtWidgets.QLabel(self.w)
        self.player_label.move(300, 100)
        self.player_label.setText("Playing: " + self.now_player.name)

    def quit_button(self):
        self.quit_button = QtWidgets.QPushButton('Add', self.w)
        self.quit_button.setText('Exit')
        self.quit_button.clicked.connect(self.app.exit)
        self.quit_button.move(10, 10)

    def start_button(self):
        button = QtWidgets.QPushButton('Add', self.w)
        button.setText('Start Game')
        button.clicked.connect(lambda: print('co'))
        button.move(100, 10)

    def forward_button(self):
        button = QtWidgets.QPushButton('Add', self.w)
        button.setText('Step Forward')
        button.clicked.connect(lambda: self.now_player.step_forward(self.arena))
        button.clicked.connect(lambda: self.update_labelerro())
        button.clicked.connect(lambda: self.change_player())
        button.move(100, 200)

    def quick_attack_button(self):
        button = QtWidgets.QPushButton('Add', self.w)
        button.setText('Quick Attack')
        button.clicked.connect(lambda: self.now_player.quick_attack(self.prev_player))
        button.clicked.connect(lambda: self.update_labelerro())
        button.clicked.connect(lambda: self.change_player())
        button.move(100, 230)

    def normal_attack_button(self):
        button = QtWidgets.QPushButton('Add', self.w)
        button.setText('Normal Attack')
        button.clicked.connect(lambda: self.now_player.normal_attack(self.prev_player))
        button.clicked.connect(lambda: self.update_labelerro())
        button.clicked.connect(lambda: self.change_player())
        button.move(200, 230)

    def power_attack_button(self):
        button = QtWidgets.QPushButton('Add', self.w)
        button.setText('Power Attack')
        button.clicked.connect(lambda: self.now_player.power_attack(self.prev_player))
        button.clicked.connect(lambda: self.update_labelerro())
        button.clicked.connect(lambda: self.change_player())
        button.move(300, 230)

    def backward_button(self):
        button = QtWidgets.QPushButton('Add', self.w)
        button.setText('Step Backward')
        button.clicked.connect(lambda: self.now_player.step_backward(self.arena))
        button.clicked.connect(lambda: self.update_labelerro())
        button.clicked.connect(lambda: self.change_player())
        button.move(200, 200)

    def update_labelerro(self):
        self.label.setText(''.join(self.arena.arena))
        self.hp_label1.setText(str(self.now_player.hp))
        self.hp_label2.setText(str(self.prev_player.hp))
        who_dead = GameManager.GameManager.is_dead(self.now_player, self.prev_player)
        if who_dead:
            endgame_text = "Player: " + who_dead + " died"
            self.label.setText(endgame_text)



    def change_player(self):
        self.now_player, self.prev_player = GameManager.GameManager.change_player(self.now_player, self.prev_player)
        self.player_label.setText("Playing: " + self.now_player.name)