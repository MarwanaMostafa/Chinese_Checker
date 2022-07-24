from msilib.schema import CheckBox
import tkinter as tk
import sys
from pygame.locals import *
from Board import *
from ProperitesBoard import *
from gui import *
from tkinter import simpledialog

def main():
    depth = 1
    ALGORITHM = 1    
    ROOT = tk.Tk()
    ROOT.withdraw()
    Level = simpledialog.askstring(
        title="LEVEL", prompt="1-Easy \n2-Medium \n3-Hard")
    if int(Level) == 1:
        depth = 1
    elif int(Level) == 2:
        depth = 2
    elif int(Level) == 3:
        depth = 3
    ROOT.destroy()
    ROOT.mainloop()

    # ROOT = tk.Tk()
    # ROOT.withdraw()
    # ALGO = simpledialog.askstring(
        # title="LEVEL", prompt="Which Alogrithm \n1-MINMAX\n2-ALPHA-BETA")
    # if int(ALGO) == 1:
        # ALGORITHM = 1
    # elif int(ALGO) == 2:
    ALGORITHM = 2
    # print(ALGORITHM)
    # ROOT.destroy()
    # ROOT.mainloop()
    p1_win = 0
    p2_win = 0

    
    board = build_board()
    player1_set, player2_set = Intalize_sets()
    player1_obj, player2_obj = buildGoalSets()
    display_surface = init_board()

    player_turn = 1

    game_over = False
    counter = 1
    FROM = []
    while True:
        draw_board(board, display_surface)
        for event in pg.event.get():

            if event.type == QUIT: 
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = pg.mouse.get_pos()

                set_pieces = assign_set(player_turn, player1_set, player2_set)
                invalid_homes_set = []
                obj_set = assignGOAlSet(player_turn, player1_obj, player2_obj)
                all_legal_moves = FindALLVALIDMOVE(
                    board, set_pieces, obj_set, invalid_homes_set)

                if player_turn == 1:
                    XIndex = int((mouse_pos[1]-(mouse_pos[1] % 40) + 20)/40)
                    YIndex = int((mouse_pos[0]-(mouse_pos[0] % 40)+20)/40)*2
                    CALC = int((mouse_pos[0] / 40)+0.5)
                    if XIndex % 2 != 0:
                        if (mouse_pos[0])/40 < CALC:
                            YIndex = 1 + \
                                int((mouse_pos[0]-(mouse_pos[0] % 40)+20)/40)*2
                        else:
                            YIndex = -1 + \
                                int((mouse_pos[0]-(mouse_pos[0] % 40)+20)/40)*2

                    if counter == 1:
                        for i in all_legal_moves:
                            if i[0] == [XIndex, YIndex]:
                                highlight_move(i, display_surface)
                                FROM = [XIndex, YIndex]
                                counter = 2
                        pg.display.update()
                    elif counter == 2:
                        for i in all_legal_moves:
                            if i[1] == [XIndex, YIndex] and i[0] == FROM:
                                best_move = i
                                # print(i)
                                board, set_pieces = MOVE(
                                    board, best_move, set_pieces)
                                player1_set, player2_set = ModifySet(
                                    set_pieces, player_turn, player1_set, player2_set)
                                pg.display.update()
                                player_turn = 2
                        counter = 1

                if player_turn == 2:
                    set_pieces = assign_set(
                        player_turn, player1_set, player2_set)
                    invalid_homes_set = []
                    obj_set = assignGOAlSet(
                        player_turn, player1_obj, player2_obj)
                    all_legal_moves = FindALLVALIDMOVE(
                        board, set_pieces, obj_set, invalid_homes_set)
                    best_move = find_move(board, all_legal_moves, obj_set, player_turn, set_pieces,
                                               player1_set, player2_set,depth,ALGORITHM)

                    pg.display.update()
                    board, set_pieces = MOVE(board, best_move, set_pieces)
                    player1_set, player2_set = ModifySet(
                        set_pieces, player_turn, player1_set, player2_set)
                    player_turn = 1

                    if best_move is None:
                        game_over = True
                        break

                    game_over = ISWin(set_pieces, obj_set)
                    if game_over:
                        if player_turn == 1:
                            p1_win = p1_win + 1
                        if player_turn == 2:
                            p2_win = p2_win + 1
                        print('Player 1 wins:', p1_win)
                        print('Player 2 wins:', p2_win)


if __name__ == '__main__':
    main()
