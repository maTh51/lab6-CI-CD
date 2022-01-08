import random

class Tic_tac_toe:

    def __init__(self):
        self.board = []
        self.two_players = False

    def new_board(self):
        self.board.clear()
        for i in range(3):
            self.board.append(['.', '.', '.'])
    
    def start(self, mode):
        
        self.new_board()

        self.two_players = mode

        # print(self.board)
        return(self.two_players)


teste = Tic_tac_toe()
teste.start(True)

