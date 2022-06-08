import pygame as pg
# 1 = PLAYER 1
PLAYER1_GREEN = (0, 255, 0)
# 2 = PLAYER 2
PLAYER2_RED = (255, 0, 0)
# board
RADIUS = 20
CIRCLE_DIAMETER = 2 * RADIUS
WINDOW_WIDTH = (CIRCLE_DIAMETER * 13)
WINDOW_HEIGHT = (CIRCLE_DIAMETER * 17)


def init_board():
    pg.init()
    display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('Chinese Checkers AI')
    return display_surface


def draw_board(board, display_surface):
    display_surface.fill((0, 0, 0))
    # لو اتغير الرسمة هتنزل لتحت اوهتطلع
    SpaceCol = RADIUS

    for ROW in range(0, 17):
        SPACE = RADIUS
        space = int(CIRCLE_DIAMETER)
        for circle_in_a_row in range(0, 13):
            if ROW % 2 == 0:
                board_value = board[ROW][circle_in_a_row * 2]
                CloroingBoard(board_value, display_surface,
                              SPACE, SpaceCol)
                SPACE = SPACE + CIRCLE_DIAMETER
            elif ROW % 2 != 0 and circle_in_a_row != 12:
                board_value = board[ROW][circle_in_a_row * 2 + 1]
                CloroingBoard(board_value, display_surface,
                              space, SpaceCol)
                space = space + CIRCLE_DIAMETER

        SpaceCol = SpaceCol + CIRCLE_DIAMETER


def CloroingBoard(board, surface, x, y):

    if board == -1:
        pg.draw.circle(surface, (0, 0, 0),
                       (x, y), RADIUS, 0)
    if board == 0:
        pg.draw.circle(surface, (255, 255, 255),
                       (x, y), RADIUS, 0)
    if board == 1:
        pg.draw.circle(surface, PLAYER1_GREEN,
                       (x, y), RADIUS, 0)
    if board == 2:
        pg.draw.circle(surface, PLAYER2_RED,
                       (x, y), RADIUS, 0)


def highlight_move(move, surface):

    [start_x, start_y] = move[0]  # source
    [end_x, end_y] = move[1]  # destination

    circle_start_x, circle_start_y = find_coordinates(start_x, start_y)
    # print("circle_start_x",circle_start_x)
    # print("circle_start_y",circle_start_y)
    pg.draw.ellipse(surface, (0, 255, 255), (circle_start_x - RADIUS, circle_start_y - RADIUS,
                                                     CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)

    circle_end_x, circle_end_y = find_coordinates(end_x, end_y)
    pg.draw.ellipse(surface, (0, 255, 255), (circle_end_x - RADIUS, circle_end_y - RADIUS,
                                                     CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)  # 5 :الدايرة تظلل قد ايه سمكها


def find_coordinates(x, y):

    if x % 2 == 0:
        circle_x = int(RADIUS +
                       (CIRCLE_DIAMETER) * (y / 2))
    else:
        circle_x = int(CIRCLE_DIAMETER + (CIRCLE_DIAMETER) * ((y - 1)
                                                              / 2))
    circle_y = RADIUS + (CIRCLE_DIAMETER) * x

    return circle_x, circle_y


def highlight_All_move(x, y, surface, move):

    [end_x, end_y] = move
    pg.draw.ellipse(surface, (0, 255, 255), (x - RADIUS, y - RADIUS,
                                                     CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)

    circle_end_x, circle_end_y = find_coordinates(end_x, end_y)
    pg.draw.ellipse(surface, (0, 255, 255), (circle_end_x - RADIUS, circle_end_y - RADIUS,
                                                     CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)  # 5 :الدايرة تظلل قد ايه سمكها
