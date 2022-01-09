from os import pipe
import random

class Tic_tac_toe:

    def __init__(self):
        self.board = []
        self.two_players = False
        self.cur_player = 'X'

    def new_board(self):
        self.board.clear()
        for i in range(3):
            self.board.append(['.', '.', '.'])

    def next_turn(self):
        if(self.cur_player == 'X'):
            self.cur_player = 'O'
        else:
            self.cur_player = 'X'

    def set_field(self, x_coord, y_coord):
        if(x_coord < 0 or x_coord > 2 or not isinstance(x_coord, int)):
            raise ValueError("Invalid coordinates (input only 1, 2 or 3)")
        elif(y_coord < 0 or y_coord > 2 or not isinstance(y_coord, int)):
            raise ValueError("Invalid coordinates (input only 1, 2 or 3)")
        elif(self.board[x_coord][y_coord] != '.'):
            raise ValueError("Field already set. Choose another")
        else:
            self.board[x_coord][y_coord] = self.cur_player
            return True

    def check_victory(self):
        win_flag = True
        for col in range(3):
            win_flag = True
            for i in range(3):
                if(self.board[i][col] != self.cur_player):
                    win_flag = False
        
            if(win_flag):
                return True

        for row in range(3):
            win_flag = True
            for i in range(3):
                if(self.board[row][i] != self.cur_player):
                    win_flag = False 
            if(win_flag):
                return True

        win_flag = True
        for diag in range(3):
            if(self.board[diag][diag] != self.cur_player):
                win_flag = False
        
        if(win_flag):
            return True

        win_flag = True
        for diag in range(3):
            if(self.board[diag][3 - 1 - diag] != self.cur_player):
                win_flag = False
        
        return win_flag

    def check_draw_game(self):
        for row in range(3):
            for col in range(3):
                if(self.board[row][col] == '.'):
                    return False
        
        return True
    
    def ia_choose_field(self):
        possibles = []
        for row in range(3):
            for col in range(3):
                if(self.board[row][col] == '.'):
                    possibles.append((row, col))

        return random.choice(possibles)
        
    def print_board(self):
        print()
        for row in self.board:
            for spot in row:
                print(spot, end=" ")
            print('\n')

    def start(self, mode):
        
        self.new_board()
        game_flag = True
        
        if(mode == False):
            # 0 = player start | 1 = IA start
            player = random.randint(0, 1)
            while(game_flag):
                if(player == 0):
                    print("Player's turn")
                    self.print_board()

                    end_turn_flag = False
                    while(not end_turn_flag):
                        x_pos, y_pos = list(
                            map(int, input("Enter row and column numbers to fix spot: ").split()))
                        print()

                        end_turn_flag = self.set_field(x_pos-1, y_pos-1)

                    if(self.check_victory()):
                        print("End game")
                        self.print_board()
                        print("Player WINS")
                        game_flag = False
                    
                    elif(self.check_draw_game()):
                        self.print_board()
                        print("Draw game")
                        game_flag = False
                    
                    else:
                        self.next_turn()
                        player = 1
                else:
                    print("IA's Turn")
                    self.print_board()
                    x, y = self.ia_choose_field()
                    self.set_field(x,y)

                    if(self.check_victory()):
                        self.print_board()
                        print("End game")
                        game_flag = False
                        print("IA Wins")
                    
                    elif(self.check_draw_game()):
                        print("Draw game")
                        self.print_board()
                        print("Draw game")
                        game_flag = False
                    
                    else:
                        self.next_turn()
                        player = 0
        else:
            # 0 = player start | 1 = IA start
            player = random.randint(0, 1)
            while(game_flag):
                if(player == 0):
                    print("Player's 1 turn")
                else:
                    print("Player's 2 turn")
                
                self.print_board()

                end_turn_flag = False
                while(not end_turn_flag):
                    x_pos, y_pos = list(
                        map(int, input("Enter row and column numbers to fix spot: ").split()))
                    print()

                    end_turn_flag = self.set_field(x_pos-1, y_pos-1)

                if(self.check_victory()):
                    print("End game")
                    self.print_board()
                    if(player == 0):
                        print("Player 1 WINS")
                    else:
                        print("Player 2 WINS")
                    game_flag = False
                
                elif(self.check_draw_game()):
                    self.print_board()
                    print("Draw game")
                    game_flag = False
                    
                else:
                    self.next_turn()
                    player = (player + 1)%2

                        