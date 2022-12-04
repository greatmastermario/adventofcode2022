import adventutils


def split_data(assignments):
    return [[[int(section) for section in assignment.split("-")]
             for assignment in pair.split(",")]
            for pair in assignments]


def full_overlap(pair):
    return pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] or \
        pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]


def partial_overlap(pair):
    return pair[0][0] in range(pair[1][0], pair[1][1] + 1) or pair[1][0] in range(pair[0][0], pair[0][1] + 1) or \
        pair[0][1] in range(pair[1][0], pair[1][1] + 1) or pair[1][1] in range(pair[0][0], pair[0][1] + 1)


def count_overlap(assignments, overlap_method):
    count = 0
    for assignment in assignments:
        if overlap_method(assignment):
            count += 1
    return count


if __name__ == "__main__":
    input_data = adventutils.file_contents("data/day04.txt")
    split_assign = split_data(input_data)
    print("Puzzle 1: " + str(count_overlap(split_assign, full_overlap)))
    print("Puzzle 2: " + str(count_overlap(split_assign, partial_overlap)))
