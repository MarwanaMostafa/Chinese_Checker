import numpy as np
from ALGORITHM import minimax,alphabeta
def build_board():
    board = np.zeros((17, 25))
    board[:][:] = -1
    board[0][12] = 1
    board[1][11] = 1
    board[1][13] = 1
    board[2][10] = 1
    board[2][12] = 1
    board[2][14] = 1
    board[3][9] =  1
    board[3][11] = 1
    board[3][13] = 1
    board[3][15] = 1

    board[4][18] = 0
    board[4][20] = 0
    board[4][22] = 0
    board[4][24] = 0
    board[5][19] = 0
    board[5][21] = 0
    board[5][23] = 0
    board[6][20] = 0
    board[6][22] = 0
    board[7][21] = 0

    board[9][21] =  0
    board[10][20] = 0
    board[10][22] = 0
    board[11][19] = 0
    board[11][21] = 0
    board[11][23] = 0
    board[12][18] = 0
    board[12][20] = 0
    board[12][22] = 0
    board[12][24] = 0

    board[13][9] =  2
    board[13][11] = 2
    board[13][13] = 2
    board[13][15] = 2
    board[14][10] = 2
    board[14][12] = 2
    board[14][14] = 2
    board[15][11] = 2
    board[15][13] = 2
    board[16][12] = 2

    board[9][ 3] =  0
    board[10][2] = 0
    board[10][4] = 0
    board[11][1] = 0
    board[11][3] = 0
    board[11][5] = 0
    board[12][0] = 0
    board[12][2] = 0
    board[12][4] = 0
    board[12][6] = 0

    board[4][0] = 0
    board[4][2] = 0
    board[4][4] = 0
    board[4][6] = 0
    board[5][1] = 0
    board[5][3] = 0
    board[5][5] = 0
    board[6][2] = 0
    board[6][4] = 0
    board[7][3] = 0

    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0

    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 0
    board[5][13] = 0
    board[5][15] = 0
    board[5][17] = 0

    board[6][6] = 0
    board[6][8] = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 0
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0

    board[9][5] = 0
    board[9][7] = 0
    board[9][9] = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0

    board[10][6] = 0
    board[10][8] = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0

    board[11][7] = 0
    board[11][9] = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

    board[12][8] = 0
    board[12][10] = 0
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board


def find_move(board, all_Valid_moves, obj_set, PlayerNUmber, set_pieces, player1_set, player2_set,depth,ALGO):
    
    # print("objsetttt",obj_set)
    # print("PlayerTUREEE",player_turn)
    # print("setPIECESSSS",set_pieces)
    # print("Player1111_set",player1_set)
    # print("Player2222222222_set",player2_set)

    OBJLEF = [i for i in obj_set +
                set_pieces if i not in obj_set or i not in set_pieces]
    
    if len(OBJLEF) == 2:
        for move in all_Valid_moves:
            start_move = move[0]
            end_move = move[1]
            if start_move == OBJLEF[1] and end_move == OBJLEF[0]:
                    return move
    try:
            if ALGO==1:
                score, best_move = minimax(board, depth, PlayerNUmber, PlayerNUmber, player1_set, player2_set)
            else:
                score, best_move = alphabeta(board, depth, PlayerNUmber, PlayerNUmber, player1_set, player2_set,-99999,99999)
        
    except Exception:
        return
    return best_move

def ISWin(set_pieces, obj_set):
    ISWIN = True
    for piece in set_pieces:
        if piece not in obj_set:
            ISWIN = False
    return ISWIN
