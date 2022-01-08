import sys, os.path 
import unittest

src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/src/')
sys.path.append(src_path)

from src.tic_tac_toe import Tic_tac_toe

class TestSum(unittest.TestCase):

    def test_sum(self):
        teste = Tic_tac_toe()
        self.assertEqual(teste.start(False), False, "Should be False")

    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 3, 2)), 6, "Should be 6")
