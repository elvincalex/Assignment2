import random
#history={0:''}
def display_board(board):
    print('  |   |   ')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('  |   |   ')
def player_input(board,e,choice,oc):
    correct_input = True
    position = int(input('User"s chance! Choose field to fill {} '.format(choice)))
    if board[position] == 'X' or board[position] == 'O':
        correct_input = False
    if not correct_input:
        print("Position already equipped")
        player_input(board,e,choice, oc)
    else:
        e.remove(position)
        board[position] = choice
        display_board(board)
        m = check_win(board)
        if m!=9:
            comp_input(board,e,oc,choice)
        else:
            play()
def comp_input(board,empty,choice,oc):
    correct_input = True
    random.shuffle(empty)
    position =list(empty)
    position=position[0]
    if board[position] == 'X' or board[position] == 'O':
        correct_input = False
    if not correct_input:
        print("Position already equipped")
        comp_input(board,empty,choice,oc)
    else:
        empty.remove(position)
        board[position] = choice
        print("Computer has entered at {}".format(position))
        display_board(board)
        n=check_win(board)
        if n!=9:
            player_input(board,empty,oc, choice)
        else:
            play()

def check_win(board):
    player_symbol = ['X', 'O']
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for check in winning_positions:
        first_symbol = board[check[0]]
        if first_symbol != ' ':
            won = True
            for point in check:
                if board[point] != first_symbol:
                    won = False
                    break
            if won:
                if first_symbol == player_symbol[0]:
                    print('User has won')
                    #history[1]={'User'}
                    #print(history)
                    return 9
                else:
                    print('Computer has won')
                    play()
                    return 9

                break
        else:
            won = False
    if won:
        return 0
    else:
        return 1

def play():
    round=1
    ch=['X','O']
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("Do you want to start the game? 1.YES 2.NO")
    k=int(input())
    while(k!=2):
        print("Round no:{}".format(round))
        print("Player's choice is X")
        while empty and check_win(board):
            if (k == 1):
                round=round+1
                display_board(board)
                player_input(board, empty, ch[0], ch[1])
        if not empty:
                print("NO WINNER!, Game tied")

if __name__ == '__main__':
    play()