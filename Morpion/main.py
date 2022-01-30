import time

def game():
    print('1 2 3\n4 5 6\n7 8 9')
    board = [['','',''],['','',''],['','','']]
    bot(board)
    return None



def player(board):
    move = int(input('\n choose a number : '))
    if board[(move-1)//3][(move-1)%3] == '':
        board[(move-1)//3][(move-1)%3] = 'X'
    else:
        player(board)
    draw_game(board)
    if check_win(board) != None:
        say_winner(check_win(board))
        return 1
    bot(board)

def bot(board):
    BestMove = [0, 0]
    BestScore = -10
    score = -10
    for i in range(3):
        for j in range(3):
            if board[j][i] == '':
                board[j][i] = 'O'
                score = minimax(board, False)
                if score >= BestScore:
                    BestMove = [j,i]
                    BestScore = score
                board[j][i] = ''
    board[BestMove[0]][BestMove[1]] = 'O'
    draw_game(board)
    if check_win(board) != None:
        say_winner(check_win(board))
        return 1
    player(board)


def minimax(board, isMaximising):
    if isMaximising:
        if check_win(board) != None:
            return check_win(board)
        Bestscore = -100
        score = 0
        for i in range(3):
            for j in range(3):
                if board[j][i] == '':
                    board[j][i] = 'O'
                    score = minimax(board, False)
                    if score > Bestscore:
                        Bestscore = score
                    board[j][i] = ''
        return Bestscore
    else:
        if check_win(board) != None:
            return check_win(board)
        Bestscore = 100
        score = 0
        for i in range(3):
            for j in range(3):
                if board[j][i] == '':
                    board[j][i] = 'X'
                    score = minimax(board, True)
                    if score < Bestscore:
                        Bestscore = score
                    board[j][i] = ''
        return Bestscore

def check_win(board):
    winner = None
    t = 0
    tab = {'X': -1, 'O':1, 'tie':0}
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1]!='':
            winner = tab[board[i][1]]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i]!='':
            winner = tab[board[1][i]]
        if not '' in board[i]:
            t += 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1]!='':
        winner = tab[board[1][1]]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1]!='':
        winner = tab[board[1][1]]
    if t == 3:
        winner = tab['tie']
    return winner

def say_winner(winner):
    tab = {-1: 'Player', 1:'Bot', 0:'Egalité'}
    print(tab[winner])
    return 1

def draw_game(board):
    print('\n')
    for i in range(3):
        print(board[i][0], '|', board[i][1], '|', board[i][2])
    print('\n', '__________________')


if __name__ == '__main__':
    game()