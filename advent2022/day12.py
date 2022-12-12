import adventutils


def maps(input_file):
    height_map = []
    for line in input_file:
        height_map.append([char for char in line])
    # distance_map = [[False for _ in range(len(height_map[0]))] for _ in range(len(height_map))]
    return height_map


def chart(height_map, start):
    mapped_coords = set()
    shortest = []
    next_shortest = []
    shortest.append(start)
    mapped_coords.add(start)
    current_distance = 0
    while True:
        current_distance += 1
        for coord in shortest:
            map_coord(height_map, mapped_coords, next_shortest, coord, (coord[0] - 1, coord[1]))
            map_coord(height_map, mapped_coords, next_shortest, coord, (coord[0] + 1, coord[1]))
            map_coord(height_map, mapped_coords, next_shortest, coord, (coord[0], coord[1] - 1))
            map_coord(height_map, mapped_coords, next_shortest, coord, (coord[0], coord[1] + 1))
        for coord in next_shortest:
            if height_map[coord[0]][coord[1]] == "E":
                return current_distance
        if len(next_shortest) == 0:
            return None
        shortest = next_shortest
        next_shortest = []


def map_coord(height_map, mapped_coords, next_shortest, origin, next_coord):
    if next_coord[0] in [-1, len(height_map)] or next_coord[1] in [-1, len(height_map[0])]:
        return
    if check(height_map, mapped_coords, origin, next_coord):
        next_shortest.append(next_coord)
        mapped_coords.add(next_coord)


def check(height_map, mapped_coords, origin, next_coord):
    if next_coord in mapped_coords:
        return False
    if height_map[next_coord[0]][next_coord[1]] == "E" and height_map[origin[0]][origin[1]] in ["y", "z"]:
        return True
    if height_map[origin[0]][origin[1]] == "S" and height_map[next_coord[0]][next_coord[1]] in ["a", "b"]:
        return True
    return height_map[next_coord[0]][next_coord[1]] not in ["E", "S"] and \
        ord(height_map[next_coord[0]][next_coord[1]]) - ord(height_map[origin[0]][origin[1]]) <= 1


def initialize(height_map):
    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            if height_map[row][col] == "S":
                return row, col


def shortest_hike(height_map):
    distances = []
    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            if height_map[row][col] in ["a", "S"]:
                distance = chart(height_map, (row, col))
                if distance:
                    distances.append(distance)
    return min(distances)


if __name__ == "__main__":
    heights = maps(adventutils.file_contents("data/day12.txt"))
    print("Puzzle 1: ", chart(heights, initialize(heights)))
    print("Puzzle 2: ", shortest_hike(heights))
