from ProperitesBoard import *
import copy

player1_set, player2_set = Intalize_sets()
player1_obj, player2_obj = buildGoalSets()

def alphabeta(board, depth, player, NUmberCallingPlayer, player1_set, player2_set, alpha, beta):
    TempBoard = board[:][:]
    if depth == 0:
        board_score = CALCULATEBOARDSCORE(
            NUmberCallingPlayer, player1_set, player2_set)
        return board_score, None

    set_pieces = assign_set(player, player1_set, player2_set)

    GoalSet = assignGOAlSet(player, player1_obj, player2_obj)

    inv_homes_set = []

    valid_moves = FindALLVALIDMOVE(
        TempBoard, set_pieces, GoalSet, inv_homes_set)

    scores = []
    moves = []

    if player == NUmberCallingPlayer:

        for move in valid_moves:

            TempBoard2 = copy.copy(TempBoard)
            new_board, new_set_pieces = MOVE(
                TempBoard2, move, set_pieces)

            player1_set, player2_set = ModifySet(
                new_set_pieces, player, player1_set, player2_set)

            next_player = player + 1
            if next_player == 3:
                next_player = 1

            score, something = alphabeta(
                new_board, depth - 1, next_player, NUmberCallingPlayer, player1_set, player2_set, alpha, beta)

            scores.append(score)
            moves.append(move)
            alpha = max(score, alpha)

            if beta <= alpha:
                break

        if len(scores) == 0:
            return
        INDEXAXSCORE = scores.index(max(scores))
        BESTMOVE = moves[INDEXAXSCORE]
        return scores[INDEXAXSCORE], BESTMOVE

    else:
        for move in valid_moves:
            TempBOard2 = copy.copy(TempBoard)
            new_board, new_set_pieces = MOVE(
                TempBOard2, move, set_pieces)

            player1_set, player2_set = \
                ModifySet(new_set_pieces, player,
                                  player1_set, player2_set)

            next_player = player + 1
            if next_player == 3:
                next_player = 1

            score, something = alphabeta(
                new_board, depth - 1, next_player, NUmberCallingPlayer, player1_set, player2_set, alpha, beta)

            scores.append(score)
            moves.append(move)
            beta = min(score, beta)
            if beta <= alpha:
                break

        if len(scores) == 0:
            return
        INDEXMINSCORE = scores.index(min(scores))
        WORST = moves[INDEXMINSCORE]
        return scores[INDEXMINSCORE], WORST




def minimax(board, depth, player, first_player, player1_set, player2_set):

    TEMPBOARD = board[:][:]

    if depth == 0:
        board_score = CALCULATEBOARDSCORE(first_player, player1_set, player2_set)
        return board_score, None


    set_pieces = assign_set(player, player1_set,player2_set)

    obj_set = assignGOAlSet(player, player1_obj, player2_obj)
    inv_homes_set = []

    valid_moves = FindALLVALIDMOVE(TEMPBOARD, set_pieces, obj_set, inv_homes_set)


#     #      -[0,12]
#     # -,[1,11]           -[1,13]
# #   -2,10      -2,12         -2,14
# # -3.9   empty    -3,13         -3,15
# # -     nodemove -   -       -
# # 5,7   5,9    5,11   5,13   5,15   5,17

# # [0.29340139870755805,[[1, 13], [3, 11]]
# # 0.48113629034061417,[[1, 13], [5, 9]
# # 0.19704264032061153,[[2, 10], [3, 11]]
# # 0.2763145659610082,  [[2, 10], [4, 8]]
# # 0.2983233934250304, [[2, 10], [4, 12]]
# # 0.2880321533983416,[[2, 12], [4, 14]]
# # 0.19229127669785234,[[2, 12], [3, 11]]
# # 0.2763145659610082, [[2, 14], [4, 16]]
# # 0.2983233934250304,[[2, 14], [4, 12]], 
# # 0.2763145659610082,[[2, 14], [4, 8]],
# # 0.10377302861055,[[3, 9], [3, 11]],
# # 0.3035404597800941, [[3, 9], [5, 11]],
# # 0.18304495425094486, [[3, 9], [4, 8]],
# # 0.09357202980226838, [[3, 13], [3, 11]],
# # 0.18931290650275762,  [[3, 13], [4, 14]],
# # 0.19485278290668723,  [[3, 13], [4, 12]], 
# # 0.10377302861055,[[3, 15], [3, 11]], 
# # # 0.2915079202436061,[[3, 15], [5, 9]],
# # 0.18304495425094486, [[3, 15], [4, 16]], 
# # 0.19951390531103924, [[3, 15], [4, 14]],
# # 0.09911190620619799,[[4, 10], [4, 12]],
# # 0.07710307874217577, [[4, 10], [4, 8]],
# # 0.19759858427132676,  [[4, 10], [5, 11]],
# # 0.18556604473483523, [[4, 10], [5, 9]],
# # -0.0021688468982173246   [[4, 10], [3, 11]]]






# [3.6797398707379196, 3.6488147885142688, 3.57973987073792, 3.6151721168448954, 3.691124555589329, 3.6455992566016824, 3.6348793310094223, 3.6141826773899375, 3.7288698521338093, 3.7288921936711414, 3.697116762984306, 3.639846739035154, 3.6031262418599193, 3.6138461674521793, 3.729308708564005, 3.6971391045216384]
# [3.6294249929792315, 3.6375874257090586, 3.6066623434854077, 3.5375874257090585, 3.629424992979231, 3.5730418046906793, 3.573019671816034, 3.684836322276056, 3.6489721105604684, 3.6034468115728213, 3.5927268859805612, 3.5720302323610764, 3.6867174071049478, 3.661178082128734, 3.654368385381875, 3.5972553889368646, 3.597233047399532, 3.5716937224233183, 3.7448875340910566, 3.7758126163147074, 3.6703104094487013, 3.6703104094487013, 3.6543906500460652]
# [3.8332073769328634, 3.833207376932863, 3.7768241886443112, 3.7413698096626904, 3.8104447274390396, 3.7413698096626904, 3.776802055769666, 3.8886187062296877, 3.8527544945141003, 3.8072291955264537, 3.7965092699341936, 3.7758126163147088, 3.89049979105858, 3.8649604660823664, 3.8250449442030354, 3.802282294709212, 3.6868197535973866, 3.727705170066857, 3.727705170066857, 3.88045627349986]
# [3.8783179676026194, 3.878317967602619, 3.821934779314067, 3.7864804003324464, 3.8555553181087956, 3.7864804003324464, 3.8219126464394217, 3.9337292968994437, 3.8701555348727914, 3.847392885378968, 3.731930344267142, 3.661993102142964, 3.772815760736613, 3.772815760736613, 3.925566864169616, 3.896347822331248, 3.8527786426264052, 3.840572671058139, 3.8210255534769018, 3.9354533055849616, 3.9105099131823176]
# [3.9040367263732176, 3.9040367263732176, 3.847653538084666, 3.812199159103045, 3.8812740768793943, 3.812199159103045, 3.847631405210021, 3.959448055670042, 3.8958742936433897, 3.8731116441495663, 3.757649103037741, 3.7985345195072115, 3.7985345195072115, 3.7985345195072115, 3.9512856229402145, 3.919978750440044, 3.879093333970573, 3.8649312431195035, 3.8469013883908745, 3.960913203413025, 3.9609353362876707]
# [4.009747495381982, 4.009747495381982, 3.95336430709343, 3.9179099281118095, 3.9869848458881583, 3.9179099281118095, 3.9533421742187844, 4.0651588246788055, 4.001585062652154, 3.9788224131583303, 3.904287883649104, 3.8633598720465048, 3.904245288515975, 3.904245288515975, 4.056996391948978, 4.0433680341767095, 3.968833504667484, 3.952848885467528, 3.9528711501317186]
# [4.025999266925107, 4.048761916418929, 3.951422142282751, 3.951422142282751, 4.090544887943485, 4.01601035843426, 4.000025739234304, 4.0000480038984945]
# [4.022921698721165, 4.045684348214988, 3.9483445740788095, 3.9483445740788095, 4.076609430438639, 4.020226242150088, 4.020204109275442, 3.93838423983299]
# [3.9982482594478146, 3.9982482594478146, 3.882785718335989, 3.9775130555713343, 3.9236711348054594, 4.006410692177642, 3.9373357744012933, 3.9158915434684607, 3.9727680205082687]
# [3.936006582224108, 3.9587692317179313, 3.9152713783476276, 3.8614294575817527, 3.989694313941582, 3.9333111256530304, 3.9332889927783854, 3.909200393891846]
# [3.9982482594478146, 3.9982482594478146, 3.882785718335989, 3.9775130555713343, 3.9236711348054594, 4.006410692177642, 3.9373357744012933, 3.9158915434684607, 3.9727680205082687]
# [3.9225304088559865, 3.94529305834981, 3.901795204979506, 3.8479532842136313, 3.9762181405734607, 3.919834952284909, 3.919812819410264, 3.837992949967812]
# [4.045029711788794, 4.045029711788794, 3.929567170676968, 4.024294507912313, 3.9704525871464385, 4.053192144518621, 3.9841172267422724, 3.9626729958094398, 3.879974184738578, 3.879974184738578, 4.019549472849247]
# [3.9754856099539913, 3.9982482594478146, 3.954750406077511, 3.900908485311636, 4.0291733416714655, 3.9727901533829137, 3.9727680205082687, 3.8909481510658166]
# [4.049172753792488, 4.049172753792488, 3.933710212680663, 4.028437549916008, 3.974595629150133, 4.057335186522316, 3.988260268745967, 3.9668160378131345, 3.8841172267422728, 4.023692514852943]

    x=1
    scores = []
    moves = []
    for move in valid_moves:
        TEMPBOARD2 = copy.copy(TEMPBOARD)
        new_board, new_set_pieces = MOVE(TEMPBOARD2, move, set_pieces)


        player1_set, player2_set = \
            ModifySet(new_set_pieces, player, player1_set, player2_set)

        next_player = player + 1
        if next_player == 3:
            next_player = 1

        score, something = minimax(new_board, depth - 1, next_player, first_player, player1_set, player2_set)

        scores.append(score)
        moves.append(move)

    if len(scores) == 0:
        return


    if player == first_player:
        # print(scores)
        INDEXMAXSCORE = scores.index(max(scores))
        BESTMOVE = moves[INDEXMAXSCORE]
        return scores[INDEXMAXSCORE], BESTMOVE

    else:
        MINSCOREINDEX = scores.index(min(scores))
        WORST = moves[MINSCOREINDEX]
        return scores[MINSCOREINDEX], WORST


def CALCULATEBOARDSCORE(NUMPLAYER, p1_pieces, p2_pieces):

    p1_avg_distance = FINDDISTANCEAVGGG(
        p1_pieces, player1_obj, 16, 12)  # 16,12goalll
    p2_avg_distance = FINDDISTANCEAVGGG(p2_pieces, player2_obj, 12, 0)
    score = CALCULATECURRENTSCORE(NUMPLAYER, p1_avg_distance, p2_avg_distance)
    return score


def FINDDISTANCEAVGGG(p_pieces, p_GOAL, _x, _y):
    total_distance = 0
    Goal_x = _x
    Goal_y = _y
    x = 1
    for obj_piece in p_GOAL:
        if obj_piece not in p_pieces:
            [Goal_x, Goal_y] = obj_piece
            break
    for piece in p_pieces:
        [x, y] = piece
        square_y = (y * 14.43) / 25
        square_obj_y = (Goal_y * 14.43) / 25
        distance_diag = math.sqrt(
            ((Goal_x - x) ** 2) + ((square_obj_y - square_y) ** 2))
        total_distance = total_distance + distance_diag
    avg_distance = total_distance / 10

    return avg_distance


def CALCULATECURRENTSCORE(Nump, Avg1p1, Avg2p2):
    score = 0
    if Nump == 1:
        pturn_avg_distance = Avg1p1
        score = ((Avg2p2 - pturn_avg_distance)) / 2
    elif Nump == 2:
        pturn_avg_distance = Avg2p2
        score = ((Avg1p1 - pturn_avg_distance))/2
    return score
