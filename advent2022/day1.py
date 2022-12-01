import adventutils


def summarize_food(puzzle_input):
    summary = list()
    total = 0
    for line in puzzle_input:
        if line == "":
            summary.append(total)
            total = 0
        else:
            total += int(line)
    return summary


if __name__ == "__main__":
    inputfile = adventutils.file_contents("data/day1.txt")
    totals = summarize_food(inputfile)
    totals.sort(reverse=True)
    print("Puzzle 1: " + str(totals[0]))
    print("Puzzle 2: " + str(sum(totals[0:3])))
