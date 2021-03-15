"""Tic Tac Tor game by Egor Iudin."""


class TicTacToe:
    """
    Implementation of Tic Tac Toe game.
    """

    def __init__(self, test=False):
        self.field = [' ']*9
        self.curr_player = None
        self.players = []
        self.flag = True
        self.test = test
        if not self.test:
            self.main_loop()

    def main_loop(self):
        """
        Main loop of the game, handels input and basic logic.
        """
        self.start_handler()

        while self.flag:
            move = input(f"Ходит игрок {self.curr_player[0]}: ")
            if move == "exit":
                print("Спасибо за игру!")
                break

            try:
                move = int(move)-1

                if (0 <= move < 9) and (self.field[move] == " "):
                    self.field[move] = self.curr_player[1]

                    if self.cross_check():
                        self.print_tic_tac_toe()
                        self.award_winner()
                        self.print_score()
                        self.play_again()

                    self.change_player()
                else:
                    print("Неправильная координата!")

            except ValueError:
                print("Нужно ввести координату!")

            if self.tie_check():
                print("Ничья!")
                self.play_again()

            if self.flag:
                self.print_tic_tac_toe()

    def start_handler(self):
        """
        Game start handler.
        """
        self.players.append([input("Имя первого (играет O) игрока: "), "O", 0])
        self.players.append([input("Имя второго (играет X) игрока: "), "X", 0])
        self.curr_player = self.players[0]

        print("Для того, чтобы закончить игру введите в процессе слово 'exit'!")
        print(
            "Для того, чтобы поставить крестик или нолик, необходимо ввести номер квадрата."
        )
        print("Пример:")

        self.print_tic_tac_toe([(i + 1)for i in range(9)])
        self.print_tic_tac_toe()

    def change_player(self):
        """
        Changes the current player.
        """
        if self.curr_player == self.players[0]:
            self.curr_player = self.players[1]
        else:
            self.curr_player = self.players[0]

    def cross_check(self):
        """
        Checks winnig combinations.
        """
        win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for combo in win_combo:
            if (self.field[combo[0]] == self.field[combo[1]]) and \
                    (self.field[combo[1]] == self.field[combo[2]]):
                if self.field[combo[0]] == self.curr_player[1]:
                    return True
                if self.test and self.field[combo[0]] == "X":
                    return True
        return False

    def award_winner(self):
        """
        Awards the winner.
        """
        print(f"Выиграл игрок -- {self.curr_player[0]}!")
        self.curr_player[2] += 1

    def tie_check(self):
        """
        Checks the draw.
        """
        if " " not in self.field and self.flag:
            return True
        return False

    def play_again(self):
        """
        Asks whether to repeat the game.
        Change game flag or clear game field depending on the answer of user.
        """
        if input("Хотите сыграть заново? (yes/no): ") == "yes":
            self.field = [' ']*9
        else:
            self.flag = False

    def print_tic_tac_toe(self, values=None):
        """
        Prints tic tac toe field.
        """
        if not values:
            values = self.field

        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
        print("\t     |     |")
        print("\n")

    def print_score(self):
        """
        Prints scoreboard.
        """
        print("\n")
        print("\t Score")
        print('\t_____________________\n')
        print("\t  {}  :  {} ".format(self.players[0][0], self.players[0][2]))
        print('\t_____________________\n')
        print("\t  {}  :  {} ".format(self.players[1][0], self.players[1][2]))
        print('\t_____________________')
        print("\n")


if __name__ == "__main__":
    game = TicTacToe()
