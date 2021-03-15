import unittest
from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe(True)
        self.tic_tac_toe.players.append(["Test1", "O", 0])
        self.tic_tac_toe.players.append(["Test2", "X", 0])
        self.tic_tac_toe.curr_player = self.tic_tac_toe.players[0]

    def test_change_player(self):
        self.assertEqual(self.tic_tac_toe.curr_player[0], "Test1")
        self.tic_tac_toe.change_player()
        self.assertEqual(self.tic_tac_toe.curr_player[0], "Test2")

    def test_cross_check(self):
        combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6),
                  (1, 5, 6), (2, 4, 8), (2, 3, 5), (1, 4, 6))
        ans = (True, True, True, True,
               True, True, True, True,
               False, False, False, False)
        for combo in zip(combos, ans):
            for pos in combo[0]:
                self.tic_tac_toe.field[pos] = "X"

            self.assertEqual(self.tic_tac_toe.cross_check(), combo[1])
            self.tic_tac_toe.field = [0]*9

    def test_tie_check(self):
        self.tic_tac_toe.field = ["X", "X", "O", "X", "X", "O", "O", "O", " "]
        self.assertEqual(self.tic_tac_toe.tie_check(), False)

        self.tic_tac_toe.field = ["X", "X", "O", "", "X", "O", " ", " ", "X"]
        self.assertEqual(self.tic_tac_toe.tie_check(), False)

        self.tic_tac_toe.field = ["X", "X", "O", "X", "X", "O", "O", "O", "X"]
        self.assertEqual(self.tic_tac_toe.tie_check(), True)


if __name__ == "__main__":
    unittest.main()
