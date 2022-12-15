import adventutils


def build_cave(input_file, with_floor=False):
    minx, maxx, maxy = min_max_coords(input_file)
    if with_floor:
        minx = min(500 - maxy - 4, minx)
        maxx = max(500 + maxy + 4, maxx)
    cave = [["." for _ in range(maxy + 1)] for _ in range(minx, maxx + 1)]
    if with_floor:
        for x in cave:
            x.extend([".", "#"])
    for line in input_file:
        start = None
        for coord in line.split(" -> "):
            point = coord.split(",")
            point = (int(point[0]), int(point[1]))
            if start and start[0] == point[0]:
                ys = sorted([start[1], point[1]])
                for y in range(ys[0], ys[1] + 1):
                    cave[start[0] - minx][y] = "#"
            elif start and start[1] == point[1]:
                xs = sorted([start[0], point[0]])
                for x in range(xs[0], xs[1] + 1):
                    cave[x - minx][start[1]] = "#"
            start = point
    return cave, minx


def min_max_coords(input_file):
    points = []
    for line in input_file:
        split = line.split(" -> ")
        for coord in split:
            points.append(coord.split(","))
    minx = min([int(coord[0]) for coord in points])
    maxx = max([int(coord[0]) for coord in points])
    maxy = max([int(coord[1]) for coord in points])
    return min(minx, 500), max(maxx, 500), maxy


def pour(cave, offset_x):
    sand_ct = 0
    into_abyss = False
    startx = 500 - offset_x
    while not into_abyss:
        x, y = startx, 0
        settled = False
        while not settled and not into_abyss:
            if y + 1 >= len(cave[0]):
                into_abyss = True
            elif cave[x][y + 1] == ".":
                y += 1
            elif x - 1 < 0:
                into_abyss = True
            elif cave[x - 1][y + 1] == ".":
                x -= 1
                y += 1
            elif x + 1 > len(cave):
                into_abyss = True
            elif cave[x + 1][y + 1] == ".":
                x += 1
                y += 1
            else:
                cave[x][y] = "o"
                sand_ct += 1
                settled = True
                if x == startx and y == 0:
                    into_abyss = True
    return sand_ct


if __name__ == "__main__":
    cave_layout, coord_offset = build_cave(adventutils.file_contents("data/day14.txt"))
    print("Puzzle 1: ", pour(cave_layout, coord_offset))
    cave_layout, coord_offset = build_cave(adventutils.file_contents("data/day14.txt"), True)
    print("Puzzle 2: ", pour(cave_layout, coord_offset))

