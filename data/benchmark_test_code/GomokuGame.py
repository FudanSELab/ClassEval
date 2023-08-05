import unittest

class GomokuGameTestMakeMove(unittest.TestCase):
    def setUp(self) -> None:
        self.board_size = 10
        self.gomokuGame = GomokuGame(self.board_size)

    def test_make_move_1(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        board[0][0] = 'X'
        self.assertEqual(board, self.gomokuGame.board)

    # same position
    def test_make_move_2(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        self.assertEqual(False, self.gomokuGame.make_move(0, 0))
        board[0][0] = 'X'
        self.assertEqual(board, self.gomokuGame.board)

    def test_make_move_3(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        self.assertEqual(True, self.gomokuGame.make_move(0, 1))
        board[0][0] = 'X'
        board[0][1] = 'O'
        self.assertEqual(board, self.gomokuGame.board)

    def test_make_move_4(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        self.assertEqual(True, self.gomokuGame.make_move(0, 1))
        self.assertEqual(False, self.gomokuGame.make_move(0, 0))
        board[0][0] = 'X'
        board[0][1] = 'O'
        self.assertEqual(board, self.gomokuGame.board)

    def test_make_move_5(self):
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.assertEqual(True, self.gomokuGame.make_move(0, 0))
        self.assertEqual(True, self.gomokuGame.make_move(0, 1))
        self.assertEqual(False, self.gomokuGame.make_move(0, 1))
        board[0][0] = 'X'
        board[0][1] = 'O'
        self.assertEqual(board, self.gomokuGame.board)


class GomokuGameTestCheckWinner(unittest.TestCase):
    def test_check_winner_1(self):
        gomokuGame = GomokuGame(10)
        self.assertEqual(None, gomokuGame.check_winner())

    def test_check_winner_2(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('X', gomokuGame.check_winner())

    def test_check_winner_3(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 0), (0, 4)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('O', gomokuGame.check_winner())

    def test_check_winner_4(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1), (0, 4)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual(gomokuGame.check_winner(), 'O')

    def test_check_winner_5(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1), (0, 4), (5, 0)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('O', gomokuGame.check_winner())


class GomokuGameTestCheckFiveInARow(unittest.TestCase):
    def setUp(self) -> None:
        self.gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            self.gomokuGame.make_move(move[0], move[1])

    def test_check_five_in_a_row_1(self):
        self.assertEqual(True, self.gomokuGame._check_five_in_a_row(5, 5, (0, -1)))

    def test_check_five_in_a_row_2(self):
        self.assertEqual(True, self.gomokuGame._check_five_in_a_row(5, 1, (0, 1)))

    def test_check_five_in_a_row_3(self):
        self.assertEqual(False, self.gomokuGame._check_five_in_a_row(0, 0, (0, 1)))

    def test_check_five_in_a_row_4(self):
        self.assertEqual(False, self.gomokuGame._check_five_in_a_row(0, 0, (1, 0)))

    def test_check_five_in_a_row_5(self):
        self.assertEqual(False, self.gomokuGame._check_five_in_a_row(5, 5, (1, 0)))

class GomokuGameTestMain(unittest.TestCase):
    def test_main(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        self.assertEqual(None, gomokuGame.check_winner())
        for move in moves:
            self.assertEqual(True, gomokuGame.make_move(move[0], move[1]))
        self.assertEqual(False, gomokuGame.make_move(0, 0))
        self.assertEqual(True, gomokuGame._check_five_in_a_row(5, 5, (0, -1)))
        self.assertEqual('X', gomokuGame.check_winner())


