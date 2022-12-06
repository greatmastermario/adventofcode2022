import adventutils


def detect_start(input_data, size):
    for index in range(len(input_data) - size):
        if len(set([char for char in input_data[index:index+size]])) == size:
            return index + size
    return 0


if __name__ == "__main__":
    data = adventutils.file_contents("data/day06.txt")
    print("Puzzle 1: " + str(detect_start(data[0], 4)))
    print("Puzzle 1: " + str(detect_start(data[0], 14)))
