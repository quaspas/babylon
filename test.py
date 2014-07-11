import unittest
from game import stack, Board


class GameSetupTests(unittest.TestCase):

    def test_start(self):
        board = Board()
        self.assertTrue(len(board.stacks), 12)


class StackingTests(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_stack_one_red_on_one_blue(self):
        red = self.board.get_colour('red')
        blue = self.board.get_colour('blue')
        new_red, new_blue = stack(red, blue)
        self.assertEqual(red.top, new_blue.top)
        self.assertEqual([], new_red)
        self.assertEqual(2, new_blue.height)