import numpy as np
import math
VISITED = 20
NOT_VISITED = 15

def Intalize_sets():
    # marbles each player
    player1_set = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12],
                   [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]  # 
    player2_set = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [
        14, 12], [14, 14], [15, 11], [15, 13], [16, 12]]  # 
   
    return player1_set, player2_set

def buildGoalSets():
    player1_obj = [[16, 12], [15, 11], [15, 13], [14, 10], [14, 14], [
        14, 12], [13, 9], [13, 15], [13, 13], [13, 11]]  # 
    player2_obj = [[0, 12], [1, 13], [1, 11], [2, 14], [2, 10],
                   [2, 12], [3, 15], [3, 9], [3, 11], [3, 13]]  # 

    return player1_obj, player2_obj


def assign_set(player_turn, player1_set, player2_set):

    set_player = player1_set

    if player_turn == 1:
        set_player = player1_set
    if player_turn == 2:
        set_player = player2_set
    return set_player

def assignGOAlSet(NumPlayer, player1_GOal, player2_GOal):

    GOal_set = player1_GOal

    if NumPlayer == 1:
        GOal_set = player1_GOal
    if NumPlayer == 2:
        GOal_set = player2_GOal
    return GOal_set

def ModifySet(pieces, NumPlayer, player1_set, player2_set):

    if NumPlayer == 1:
        player1_set = pieces
    if NumPlayer == 2:
        player2_set = pieces

    return player1_set, player2_set


def FindALLVALIDMOVE(board, pieces, Goalset, invalid_homes_set):
    valid_moves = []

    for piece in pieces:
        # if piece not in obj_set:
        color_board = np.full(board.shape, NOT_VISITED)
        valid_moves = check_moves(
            board, color_board, piece, 0, piece, valid_moves)  # valid moves :contain only marbles which can move
        # [[[2, 10], [4, 12]], [[2, 10], [4, 8]],

#  [[[2, 10], [4, 12]], [[2, 10], [4, 8]],
#  [[2, 12], [4, 14]], [[2, 12], [4, 10]],
#  [[2, 14], [4, 16]], [[2, 14], [4, 12]],
#  [[3, 9], [4, 10]], [[3, 9], [4, 8]],
#  [[3, 11], [4, 12]], [[3, 11], [4, 10]],
#  [[3, 13], [4, 14]], [[3, 13], [4, 12]],
#  [[3, 15], [4, 16]], [[3, 15], [4, 14]]]

    # valid_moves = valid_move_in_house(valid_moves, invalid_set, obj_set)
    valid_moves = VALIDMOVES(valid_moves, Goalset)
# # [[[0, 12], [2, 14]], [[0, 12], [4, 12]], 
# # [[1, 13], [2, 14]], 
# # [[2, 10], [2, 14]], [[2, 10], [4, 12]], [[2, 10], [4, 12]], [[2, 10], [4, 8]], 
# # [[2, 12], [2, 14]], [[2, 12], [4, 14]], [[2, 12], [4, 10]],
# #  [[3, 9], [4, 10]], [[3, 9], [4, 8]], [[3, 11], [4, 12]], [[3, 11], [4, 10]],
# #  [[3, 13], [4, 14]], [[3, 13], [4, 12]], [[3, 13], [2, 14]],
# #  [[3, 15], [5, 17]], [[3, 15], [4, 14]], [[3, 15], [2, 14]], 
# # [[4, 16], [4, 14]], [[4, 16], [5, 17]], [[4, 16], [5, 15]], [[4, 16], [2, 14]], [[4, 16], [4, 12]]]

# # [[[1, 13], [3, 15]], [[1, 13], [5, 13]],
# #  [[2, 10], [4, 12]], [[2, 10], [4, 16]], [[2, 10], [4, 8]], 
# # [[2, 12], [4, 10]], [[2, 14], [3, 15]], [[2, 14], [4, 12]], [[2, 14], [4, 16]], 
# # [[3, 9], [4, 10]], [[3, 9], [4, 8]],
# # [[3, 11], [3, 15]], [[3, 11], [5, 13]], [[3, 11], [4, 12]], [[3, 11], [4, 10]], 
# # [[3, 13], [3, 15]], [[3, 13], [5, 15]], [[3, 13], [4, 12]], 
# # [[4, 14], [4, 16]], [[4, 14], [4, 12]], [[4, 14], [5, 15]], [[4, 14], [5, 13]], [[4, 14], [3, 15]]]


    return valid_moves


def check_moves(board, color_board, start, depth, origin, v_moves):

    # set(which has role to play ) which we must choose best node to move
    [x_v0, y_v0] = start
    color_board[x_v0][y_v0] = VISITED
    neighbors_list = neighbors(start)
    for x_v1, y_v1 in neighbors_list:  # filterrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
        if depth == 0 and board[x_v1][y_v1] == 0:
            v_moves.append([start, [x_v1, y_v1]])

        if depth == 0 and board[x_v1][y_v1] > 0:
            x_v2, y_v2 = JumbIN(start, x_v1, y_v1)
            if board[x_v2][y_v2] == 0:
                v_moves.append([start, [x_v2, y_v2]])
                v_moves = check_moves(board, color_board, [
                                      x_v2, y_v2], depth + 1, origin, v_moves)
        if depth > 0 and board[x_v1][y_v1] > 0:
            x_v2, y_v2 = JumbIN(start, x_v1, y_v1)
            if board[x_v2][y_v2] == 0 and color_board[x_v2][y_v2] == NOT_VISITED:
                v_moves.append([origin, [x_v2, y_v2]])
                v_moves = check_moves(board, color_board, [
                                      x_v2, y_v2], depth + 1, origin, v_moves)
    return v_moves


def neighbors(node):
    [x, y] = node
    neighbors = []
    temp = [x, y + 2]

    if 0 <= temp[1] <= 24:
        neighbors.append([x, y + 2])

    temp = [x, y - 2]
    if 0 <= temp[1] <= 24:
        neighbors.append([x, y - 2])
    temp = [x + 1, y + 1]

    if 0 <= temp[0] <= 16 and 0 <= temp[1] <= 24:
        neighbors.append([x + 1, y + 1])
    temp = [x + 1, y - 1]

    if 0 <= temp[0] <= 16 and 0 <= temp[1] <= 24:
        neighbors.append([x + 1, y - 1])
    temp = [x - 1, y + 1]

    if 0 <= temp[0] <= 16 and 0 <= temp[1] <= 24:
        neighbors.append([x - 1, y + 1])
    temp = [x - 1, y - 1]

    if 0 <= temp[0] <= 16 and 0 <= temp[1] <= 24:
        neighbors.append([x - 1, y - 1])
    return neighbors


def JumbIN(start, x_1, y_1):

    [start_x, start_y] = start

    x_v2 = x_1 + (x_1 - start_x)
    y_v2 = y_1 + (y_1 - start_y)

    if 0 <= x_v2 <= 16 and 0 <= y_v2 <= 24:
        return x_v2, y_v2
    else:
        return 0, 0


def VALIDMOVES(valid_moves, obj_set):
#  [[2, 10], [4, 12]], [[2, 10], [4, 8]],
#  [[2, 12], [4, 14]], [[2, 12], [4, 10]],
#  [[2, 14], [4, 16]], [[2, 14], [4, 12]],
#  [[3, 9], [4, 10]], [[3, 9], [4, 8]],
#  [[3, 11], [4, 12]], [[3, 11], [4, 10]],
#  [[3, 13], [4, 14]], [[3, 13], [4, 12]],
#  [[3, 15], [4, 16]], [[3, 15], [4, 14]]

# [[16, 12], [15, 11], [15, 13], [14, 10], [14, 14], [14, 12], [13, 9], [13, 15], [13, 13], [13, 11]] objset

    RemoveMove = []
    for valid_move in valid_moves:
        start_move = valid_move[0]#[2,10]
        end_move = valid_move[1]#[4,12]
        if start_move in obj_set:

            start_y = (start_move[1] * 14.43) / 25
            end_y = (end_move[1] * 14.43) / 25
            central_pos = (12 * 14.43) / 25
            st_diag = math.sqrt(
                ((8 - start_move[0]) ** 2) + ((central_pos - start_y) ** 2))
            end_diag = math.sqrt(
                ((8 - end_move[0]) ** 2) + ((central_pos - end_y) ** 2))
            if st_diag > end_diag:
                RemoveMove.append(valid_move)

    new_valid_moves = [i for i in valid_moves +RemoveMove if i not in valid_moves or i not in RemoveMove]
    # print(new_valid_moves)
    return new_valid_moves

def MOVE(board, move, pieces):
    [start_x, start_y] = move[0]#0,12
    [end_x, end_y] = move[1]#2,14

    piece = board[start_x][start_y]
    board[start_x][start_y] = 0#هنا صفر المكان اللى هشيل منه النود 
    board[end_x][end_y] = piece#هنا  بغير القيمة اللى فى المكان ده ولاحظ ان انا بعمل كل ده فى نسخة من البوردة الاصلية مش البورده نفسها
    remove = [[start_x, start_y]]
    new_set_pieces = [i for i in pieces +
                      remove if i not in pieces or i not in remove]
    new_set_pieces.append([end_x, end_y])
    return board, new_set_pieces
