"""
Rules:

    Babylon is a simple and fast-playing brain teaser for two players.

    The game consists of twelve tiles in four colors, and the tiles are scattered on the table at the start of play,
    creating twelve stacks that are each one tile high. On a turn, you take one stack and place it on another stack
    that is either (a) the same height or (b) topped by a tile of the same color. Stacks cannot be divided.

    Players take turns until one player cannot make a move; that player loses the game and the other player wins.

    First player to win two out of three rounds winning the game.
"""
from collections import defaultdict
import sys


def stackable(top, bottom):
    if top.height == bottom.height:
        return True
    elif top.top == bottom.top:
        return True
    else:
        return False


def stack(top, bottom):
    if stackable(top, bottom):
        bottom.extend(top)
        top = []
        return top, bottom


class Stack(list):

    def __init__(self, colour):
        super(Stack, self).__init__()
        self.append(colour)

    @property
    def height(self):
        return len(self)

    @property
    def top(self):
        return self[-1]


class Board(object):

    stacks = defaultdict()

    _colours_ = ['red', 'blue', 'green', 'purple']

    for i, colour in enumerate(_colours_*3):
        stacks[i] = Stack(colour)

    def get_colour(self, colour):
        for k, v in self.stacks.iteritems():
            if v.top == colour:
                return v


class Game(object):

    def __init__(self):
        self.board = Board()

    def print_board(self):
        for stack in self.board.stacks.iteritems():
            print stack

    def start(self):
        while True:
            self.print_board()
            sys.stdout.write("What do?:")
            choice = raw_input().lower().split(' ')
            if choice and stackable(self.board.stacks[int(choice[0])], self.board.stacks[int(choice[1])]):
                stack(self.board.stacks[int(choice[0])], self.board.stacks[int(choice[1])])
                del self.board.stacks[int(choice[0])]


if __name__ == '__main__':
    Game().start()