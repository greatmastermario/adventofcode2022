import adventutils


def simulate(moves, size):
    rope = [[0, 0] for _ in range(size)]
    visited = {(0, 0)}
    for move in moves:
        direction, distance = move.split(" ")
        for _ in range(int(distance)):
            if direction == "U":
                rope[0][1] += 1
            elif direction == "D":
                rope[0][1] -= 1
            elif direction == "L":
                rope[0][0] -= 1
            elif direction == "R":
                rope[0][0] += 1
            normalize(rope, visited)
    return len(visited)


def normalize(rope, tail_visited):
    for idx in range(len(rope) - 1):
        head_pos = rope[idx]
        tail_pos = rope[idx + 1]
        if head_pos[1] - tail_pos[1] > 1:
            if tail_pos[0] < head_pos[0]:
                tail_pos[0] += 1
            elif tail_pos[0] > head_pos[0]:
                tail_pos[0] -= 1
            tail_pos[1] += 1
        elif tail_pos[1] - head_pos[1] > 1:
            if tail_pos[0] < head_pos[0]:
                tail_pos[0] += 1
            elif tail_pos[0] > head_pos[0]:
                tail_pos[0] -= 1
            tail_pos[1] -= 1
        elif tail_pos[0] - head_pos[0] > 1:
            if tail_pos[1] < head_pos[1]:
                tail_pos[1] += 1
            elif tail_pos[1] > head_pos[1]:
                tail_pos[1] -= 1
            tail_pos[0] -= 1
        elif head_pos[0] - tail_pos[0] > 1:
            if tail_pos[1] < head_pos[1]:
                tail_pos[1] += 1
            elif tail_pos[1] > head_pos[1]:
                tail_pos[1] -= 1
            tail_pos[0] += 1
    tail_visited.add((rope[-1][0], rope[-1][1]))


if __name__ == "__main__":
    move_list = adventutils.file_contents("data/day09.txt")
    print("Puzzle 1: ", simulate(move_list, 2))
    print("Puzzle 1: ", simulate(move_list, 10))
