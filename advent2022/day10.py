import adventutils


def run(instruction_set):
    cycle = 0
    x = 1
    strength = 0
    crt = []
    for instruction in instruction_set:
        if cycle > 240:
            break
        if instruction == "noop":
            cycle += 1
            draw(crt, cycle, x)
            if cycle == 20 or (cycle - 20) % 40 == 0:
                strength += cycle * x
        else:
            to_add = instruction.split(" ")
            cycle += 1
            draw(crt, cycle, x)
            if cycle == 20 or (cycle - 20) % 40 == 0:
                strength += cycle * x
            cycle += 1
            draw(crt, cycle, x)
            if cycle == 20 or (cycle - 20) % 40 == 0:
                strength += cycle * x
            x += int(to_add[1])
    return strength, crt


def draw(crt, cycle, x):
    if (cycle - 1) % 40 in [x - 1, x, x + 1]:
        crt.append("#")
    else:
        crt.append(" ")


def print_crt(crt):
    for row in range(6):
        print("".join(crt[40 * row:40 * (row + 1) - 1]))


if __name__ == "__main__":
    instructions = adventutils.file_contents("data/day10.txt")
    signal, display = run(instructions)
    print("Puzzle 1: ", signal)
    print("Puzzle 2:")
    print_crt(display)
