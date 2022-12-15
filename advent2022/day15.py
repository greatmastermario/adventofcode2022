import adventutils


def parse_locations(input_file):
    locations = []
    for line in input_file:
        split_text = line.split(" ")
        locations.append((int(split_text[2].split("=")[-1][:-1]), int(split_text[3].split("=")[-1][:-1]),
                          int(split_text[-2].split("=")[-1][:-1]), int(split_text[-1].split("=")[-1])))
    return locations


def blocked_for_line(locations, line, remove_known=True, tuner=lambda x: True):
    blocked = set()
    found = set()
    for location in locations:
        beacon_dist = abs(location[0] - location[2]) + abs(location[1] - location[3])
        if abs(location[1] - line) <= beacon_dist:
            block_dist = beacon_dist - abs(location[1] - line)
            for x in range(location[0] - block_dist, location[0] + block_dist + 1):
                if tuner(x):
                    blocked.add(x)
        if location[3] == line and remove_known:
            found.add(location[2])
    blocked = blocked.difference(found)
    return blocked


def tune(locations, min_coord, max_coord):
    for y in range(min_coord, max_coord + 1):
        x = min_coord
        for cover in covered(locations, y):
            if x in range(cover[0], cover[1] + 1):
                x = cover[1] + 1
        if x <= max_coord:
            return x * 4000000 + y


def covered(locations, line):
    ranges = []
    for location in locations:
        beacon_dist = abs(location[0] - location[2]) + abs(location[1] - location[3])
        if abs(location[1] - line) <= beacon_dist:
            block_dist = beacon_dist - abs(location[1] - line)
            ranges.append((location[0] - block_dist, location[0] + block_dist))
    return sorted(ranges)


if __name__ == "__main__":
    locs = parse_locations(adventutils.file_contents("data/day15.txt"))
    print("Puzzle 1: ", len(blocked_for_line(locs, 2000000)))
    print("Puzzle 2: ", tune(locs, 0, 4000000))
