import adventutils


def parse_stacks(input_data):
    data = adventutils.file_contents(input_data)
    data_rows = list()
    instruction_rows = list()
    data_read = False
    crate_cols = None
    for line in data:
        if not data_read:
            if not line.startswith(" 1"):
                data_rows.append(line)
            else:
                data_read = True
                crate_cols = organize_crates(data_rows, int(line.split(" ")[-1]))
        elif line == "":
            continue
        else:
            split = line.split(" ")
            instruction_rows.append([int(split[1]), int(split[3]), int(split[5])])
    return crate_cols, instruction_rows


def organize_crates(data_rows, num_cols):
    cols = list()
    data_rows.reverse()
    for _ in range(num_cols):
        cols.append(list())
    for row in data_rows:
        for index in range(num_cols):
            if 1+index*4 < len(row) and row[1+index*4] != " ":
                cols[index].append(row[1+index*4])
    return cols


def reorganize_crates(crate_cols, instructions):
    for instruction in instructions:
        for _ in range(instruction[0]):
            crate_cols[instruction[2] - 1].append(crate_cols[instruction[1] - 1].pop())


def reorganize_crates_9001(crate_cols, instructions):
    for instruction in instructions:
        to_add = list()
        for _ in range(instruction[0]):
            to_add.append(crate_cols[instruction[1] - 1].pop())
        to_add.reverse()
        crate_cols[instruction[2] - 1].extend(to_add)


if __name__ == "__main__":
    columns, instruct = parse_stacks("data/day05.txt")
    reorganize_crates(columns, instruct)
    print("Puzzle 1: " + str([col[-1] for col in columns]))
    columns, instruct = parse_stacks("data/day05.txt")
    reorganize_crates_9001(columns, instruct)
    print("Puzzle 1: " + str([col[-1] for col in columns]))
