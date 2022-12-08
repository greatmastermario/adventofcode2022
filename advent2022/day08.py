import adventutils


def grid(lines):
    return [[int(height) for height in line] for line in lines]


def visible_in_row(forest, row, col):
    if col == 0 or col == len(forest[0]) - 1:
        return True
    tree = forest[row][col]
    return tree > max(forest[row][:col]) or tree > max(forest[row][col + 1:])


def visible_in_col(forest, row, col):
    if row == 0 or row == len(forest) - 1:
        return True
    tree = forest[row][col]
    return tree > max([frow[col] for idx, frow in enumerate(forest) if idx < row]) or \
        tree > max([frow[col] for idx, frow in enumerate(forest) if idx > row])


def count_visible(forest):
    count = 0
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            if visible_in_col(forest, row, col) or visible_in_row(forest, row, col):
                count += 1
    return count


def scenic_score(forest, row, col):
    height = forest[row][col]
    if row == 0 or row == len(forest) - 1 or col == 0 or col == len(forest[0]) - 1:
        return 0
    score = 1
    multiplier = 1
    for fcol in range(col - 1, 0, -1):
        if forest[row][fcol] < height:
            multiplier += 1
        else:
            break
    score *= multiplier
    multiplier = 1
    for fcol in range(col + 1, len(forest[0]) - 1):
        if forest[row][fcol] < height:
            multiplier += 1
        else:
            break
    score *= multiplier
    multiplier = 1
    for frow in range(row - 1, 0, -1):
        if forest[frow][col] < height:
            multiplier += 1
        else:
            break
    score *= multiplier
    multiplier = 1
    for frow in range(row + 1, len(forest) - 1):
        if forest[frow][col] < height:
            multiplier += 1
        else:
            break
    score *= multiplier
    return score


def max_scenic_score(forest):
    max_score = 0
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            max_score = max(max_score, scenic_score(forest, row, col))
    return max_score


if __name__ == "__main__":
    forest_input = grid(adventutils.file_contents("data/day08.txt"))
    print("Puzzle 1: " + str(count_visible(forest_input)))
    print("Puzzle 1: " + str(max_scenic_score(forest_input)))
