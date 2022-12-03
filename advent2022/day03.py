import adventutils


def sum_mixups(sacks):
    mix_sum = 0
    for sack in sacks:
        split = split_sack(sack)
        for part in split:
            part.sort(key=ord)
        for char in split[0]:
            if char in split[1]:
                mix_sum += priority(char)
                break
    return mix_sum


def split_sack(sack):
    split = list()
    part = list()
    for index, char in enumerate(sack):
        if index == len(sack) / 2:
            split.append(part)
            part = list()
        part.append(char)
    split.append(part)
    return split


def priority(char):
    if char.islower():
        return ord(char) - ord("a") + 1
    elif char.isupper():
        return ord(char) - ord("A") + 27
    return 0


def sum_badges(sacks):
    group = list()
    badge_sum = 0
    for index, sack in enumerate(sacks):
        group.append([char for char in sack])
        for group_sack in group:
            group_sack.sort(key=ord)
        if index % 3 == 2:
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    badge_sum += priority(char)
                    break
            group.clear()
    return badge_sum


if __name__ == "__main__":
    input_data = adventutils.file_contents("data/day03.txt")
    print("Part 1: " + str(sum_mixups(input_data)))
    print("Part 2: " + str(sum_badges(input_data)))
