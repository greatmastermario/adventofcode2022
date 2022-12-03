import adventutils


def score(input_rounds, convert_method):
    current_score = 0
    for current_round in input_rounds:
        moves = current_round.split(" ")
        final_move = convert_method(moves)
        current_score += choice_score(final_move[1])
        current_score += compare_score(final_move)
    return current_score


def choice_score(move):
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    elif move == "Z":
        return 3
    else:
        print("Bad value: " + move)
        return 0


def compare_score(move):
    if move[0] == "A" and move[1] == "Y" or move[0] == "B" and move[1] == "Z" or move[0] == "C" and move[1] == "X":
        return 6
    elif move[0] == "A" and move[1] == "X" or move[0] == "B" and move[1] == "Y" or move[0] == "C" and move[1] == "Z":
        return 3
    elif move[0] == "A" and move[1] == "Z" or move[0] == "B" and move[1] == "X" or move[0] == "C" and move[1] == "Y":
        return 0
    else:
        print("Bad values: " + move)
        return 0


def identity(move):
    return move


def convert_by_win(move):
    if move[0] == "A" and move[1] == "Y":
        return ["A", "X"]
    elif move[0] == "A" and move[1] == "Z":
        return ["A", "Y"]
    elif move[0] == "A" and move[1] == "X":
        return ["A", "Z"]
    elif move[0] == "B" and move[1] == "Y":
        return ["B", "Y"]
    elif move[0] == "B" and move[1] == "Z":
        return ["B", "Z"]
    elif move[0] == "B" and move[1] == "X":
        return ["B", "X"]
    elif move[0] == "C" and move[1] == "Y":
        return ["C", "Z"]
    elif move[0] == "C" and move[1] == "Z":
        return ["C", "X"]
    elif move[0] == "C" and move[1] == "X":
        return ["C", "Y"]
    else:
        print("Bad values: " + move)
        return 0


if __name__ == "__main__":
    rounds = adventutils.file_contents("data/day02.txt")
    print("Part 1: " + str(score(rounds, identity)))
    print("Part 2: " + str(score(rounds, convert_by_win)))
