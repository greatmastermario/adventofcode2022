import adventutils


def monkeys(puzzle_input):
    monkey_list = []
    monkey = {"inspections": 0}
    for line in puzzle_input:
        if line.startswith("Monkey"):
            continue
        elif line.startswith("  Starting items"):
            monkey["items"] = [int(item) for item in line.split(": ")[1].split(", ")]
        elif line.startswith("  Operation"):
            monkey["operation"] = [value for value in line.split("= ")[1].split(" ")]
        elif line.startswith("  Test"):
            monkey["test"] = int(line.split(" ")[-1])
        elif line.startswith("    If true"):
            monkey[True] = int(line.split(" ")[-1])
        elif line.startswith("    If false"):
            monkey[False] = int(line.split(" ")[-1])
        elif line == "":
            monkey_list.append(monkey)
            monkey = {"inspections": 0}
    monkey_list.append(monkey)
    return monkey_list


def keep_away(monkey_list, rounds, manageable):
    test_lcm = lcm(monkey_list)
    for curr_round in range(rounds):
        for monkey in monkey_list:
            for item in monkey["items"]:
                new_item = new_worry(item, monkey["operation"])
                new_item = new_item // 3 if manageable else new_item
                new_item = new_item % test_lcm
                monkey_list[monkey[new_item % monkey["test"] == 0]]["items"].append(new_item)
                monkey["inspections"] += 1
            monkey["items"].clear()
        if curr_round % 100 == 0:
            print("Round ", curr_round)


def new_worry(item, operation):
    value1 = item if operation[0] == "old" else int(operation[0])
    value2 = item if operation[2] == "old" else int(operation[2])
    return value1 + value2 if operation[1] == "+" else value1 * value2


def interaction_size(monkey):
    return monkey["inspections"]


def lcm(monkey_list):
    multiple = 1
    for monkey in monkey_list:
        multiple *= monkey["test"]
    return multiple


if __name__ == "__main__":
    all_monkeys = monkeys(adventutils.file_contents("data/day11.txt"))
    keep_away(all_monkeys, 20, True)
    all_monkeys.sort(key=interaction_size, reverse=True)
    print("Puzzle 1: ", all_monkeys[0]["inspections"] * all_monkeys[1]["inspections"])
    all_monkeys = monkeys(adventutils.file_contents("data/day11.txt"))
    keep_away(all_monkeys, 10000, False)
    all_monkeys.sort(key=interaction_size, reverse=True)
    print("Puzzle 2: ", all_monkeys[0]["inspections"] * all_monkeys[1]["inspections"])
