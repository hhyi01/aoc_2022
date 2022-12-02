with open("day02_input.txt") as f:
    games = f.readlines()

opponent_move = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

my_move = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

shape_points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

outcome_points = {
    "lost": 0,
    "draw": 3,
    "won": 6
}

game_end = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

# Rock defeats Scissors
# Scissors defeat Paper
# Paper defeats Rock


def calc_score_helper(opponent, me):
    if opponent == me:
        return outcome_points["draw"]
    elif (opponent == "Rock" and me == "Scissors") or (opponent == "Paper" and me == "Rock") \
            or (opponent == "Scissors" and me == "Paper"):
        return outcome_points["lost"]
    elif (opponent == "Rock" and me == "Paper") or (opponent == "Scissors" and me == "Rock") \
            or (opponent == "Paper" and me == "Scissors"):
        return outcome_points["won"]
    else:
        print("Missed scenario.")
        print("Opponent: " + opponent)
        print("Me: " + me)
        return


def calc_score_1(game_rounds):
    my_total_score = 0
    for game in game_rounds:
        moves = game.strip().split(" ")
        opponent = opponent_move[moves[0]]
        me = my_move[moves[1]]
        my_total_score += shape_points[me]
        my_total_score += calc_score_helper(opponent, me)
    return my_total_score


# puzzle 1
print(calc_score_1(games))


def calc_score_2(game_rounds):
    my_total_score = 0
    for game in game_rounds:
        moves = game.strip().split(" ")
        opponent = opponent_move[moves[0]]
        exp_end = game_end[moves[1]]
        if exp_end == "draw":
            me = opponent
        elif exp_end == "lose":
            if opponent == "Rock":
                me = "Scissors"
            if opponent == "Scissors":
                me = "Paper"
            if opponent == "Paper":
                me = "Rock"
        else:
            if opponent == "Rock":
                me = "Paper"
            if opponent == "Scissors":
                me = "Rock"
            if opponent == "Paper":
                me = "Scissors"
        my_total_score += shape_points[me]
        my_total_score += calc_score_helper(opponent, me)
    return my_total_score


# puzzle 2
print(calc_score_2(games))
