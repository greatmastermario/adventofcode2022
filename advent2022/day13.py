import adventutils
import functools


def group(input_file):
    signals = []
    left = None
    right = None
    for line in input_file:
        if left is None:
            left, _ = parse(line)
        elif right is None:
            right, _ = parse(line)
        elif line == "":
            signals.append((left, right))
            left = None
            right = None
    signals.append((left, right))
    return signals


def parse(line, idx=1):
    arr = []
    num_str = ""
    while idx < len(line):
        if line[idx] == "[":
            item, end_idx = parse(line, idx + 1)
            arr.append(item)
            idx = end_idx
        elif line[idx] == "]":
            if num_str != "":
                arr.append(int(num_str))
            return arr, idx
        elif line[idx] == "," and num_str != "":
            arr.append(int(num_str))
            num_str = ""
        elif line[idx] != ",":
            num_str += line[idx]
        idx += 1


def validate(signals):
    idx_sum = 0
    for idx, signal in enumerate(signals):
        if compare(signal[0], signal[1]) < 0:
            idx_sum += idx + 1
    return idx_sum


def compare(left, right):
    idx = 0
    while idx < len(left) and idx < len(right):
        if type(left[idx]) == int and type(right[idx]) == int:
            if left[idx] < right[idx]:
                return -1
            if right[idx] < left[idx]:
                return 1
        else:
            result = compare([left[idx]] if type(left[idx]) == int else left[idx],
                             [right[idx]] if type(right[idx]) == int else right[idx])
            if result != 0:
                return result
        idx += 1
    if len(left) < len(right):
        return -1
    if len(right) < len(left):
        return 1
    return 0


def decode(signals):
    all_signals = []
    for pair in signals:
        all_signals.append(pair[0])
        all_signals.append(pair[1])
    all_signals.append([[2]])
    all_signals.append([[6]])
    all_signals.sort(key=functools.cmp_to_key(compare))
    return (all_signals.index([[2]]) + 1) * (all_signals.index([[6]]) + 1)


if __name__ == "__main__":
    signal_list = group(adventutils.file_contents("data/day13.txt"))
    print("Puzzle 1: ", validate(signal_list))
    print("Puzzle 2: ", decode(signal_list))
