import sys, os.path 
import unittest

src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/src/')
sys.path.append(src_path)

from src.tic_tac_toe import Tic_tac_toe

class Test_ttt(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self._ttt = Tic_tac_toe()

    def test_check_victory(self):
        self._ttt.new_board()
        self._ttt.set_field(0, 0)
        self._ttt.set_field(0, 1)
        self._ttt.set_field(0, 2)
        self.assertEqual(self._ttt.check_victory(), True, "Should win on complete row")

    def test_check_no_victory(self):
        self._ttt.new_board()
        self.assertEqual(self._ttt.check_victory(), False, "Nobody should win on start of the game")
    
    def test_check_draw_game(self):
        self._ttt.new_board()
        self._ttt.set_field(0, 0)
        self._ttt.set_field(1, 1)
        self._ttt.set_field(2, 1)
        self._ttt.set_field(0, 2)
        self._ttt.set_field(1, 2)
        self._ttt.next_turn()
        self._ttt.set_field(0, 1)
        self._ttt.set_field(1, 0)
        self._ttt.set_field(2, 0)
        self._ttt.set_field(2, 2)
        self._ttt.next_turn()
        self.assertEqual(self._ttt.check_draw_game(), True, "All fields set without any win should be a draw")
    
    def test_check_no_draw_game(self):
        self._ttt.new_board()
        self.assertEqual(self._ttt.check_draw_game(), False, "Start of the game is not draw")

    def test_print_set_field(self):
        self._ttt.new_board()
        self._ttt.set_field(0, 0)
        self.assertEqual(self._ttt.board, [['X','.','.'],['.','.','.'],['.','.','.']], "In the start of the game, the field is empty")

    def test_print_empty_board(self):
        self._ttt.new_board()
        self.assertEqual(self._ttt.board, [['.','.','.'],['.','.','.'],['.','.','.']], "Not empty after a set")
    
    def test_initial_symbol(self):
        self._ttt.new_board()
        self.assertEqual(self._ttt.cur_player, 'X', "Start symbol should be 'X'")

    def test_next_symbol(self):
        self._ttt.new_board()
        self._ttt.next_turn()
        self.assertEqual(self._ttt.cur_player, 'O', "Next symbol should be 'O'")
        self._ttt.next_turn()
        
    def test_wrong_input(self):
        self._ttt.new_board()
        with self.assertRaises(Exception):
            self._ttt.set_field(0, 3)
    
    def test_ia_choose_field(self):
        self._ttt.new_board()
        ia_possible = self._ttt.ia_choose_field()
        self.assertTrue(ia_possible[0] <= 2 and ia_possible[0] >= 0 and ia_possible[1] <= 2 and ia_possible[1] >= 0 )
        