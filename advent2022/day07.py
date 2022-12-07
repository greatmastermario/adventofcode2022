import adventutils


def build_directory_tree(console):
    root = {}
    path = [root]
    for line in console:
        if line.startswith("$ cd"):
            if line.endswith("/"):
                path = [root]
            elif line.endswith(".."):
                path = path[:-1]
            else:
                path.append(path[-1][line.split(" ")[2]])
        elif not line.startswith("$"):
            location = line.split(" ")
            if location[0] == "dir":
                if location[1] not in path[-1].keys():
                    path[-1][location[1]] = {}
            else:
                path[-1][location[1]] = int(location[0])
    return root


def sum_sizes(file_system, max_size):
    current_size = 0
    sum_size = 0
    for value in file_system.values():
        if type(value) == int:
            current_size += value
        else:
            dir_size, dir_sum_size = sum_sizes(value, max_size)
            current_size += dir_size
            sum_size += dir_sum_size
    if current_size <= max_size:
        sum_size += current_size
    return current_size, sum_size


def get_dir_sizes(file_system):
    sizes = set()
    current_size = 0
    for value in file_system.values():
        if type(value) == int:
            current_size += value
        else:
            dir_size, size_set = get_dir_sizes(value)
            current_size += dir_size
            sizes = sizes.union(size_set)
    sizes.add(current_size)
    return current_size, sizes


def find_smallest_in_range(sizes, min_size):
    sizes_in_range = []
    for size in sizes:
        if size >= min_size:
            sizes_in_range.append(size)
    return min(sizes_in_range)


if __name__ == "__main__":
    console_output = adventutils.file_contents("data/day07.txt")
    directory = build_directory_tree(console_output)
    _, total_in_range = sum_sizes(directory, 100000)
    print("Puzzle 1: " + str(total_in_range))
    root_size, possible_sizes = get_dir_sizes(directory)
    unused = 70000000 - root_size
    print("Puzzle 2:" + str(find_smallest_in_range(possible_sizes, 30000000 - unused)))
