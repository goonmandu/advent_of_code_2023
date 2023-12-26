from typing import TextIO, Any
from copy import deepcopy


def parse(file: TextIO) -> list[str]:
    return [line.strip() for line in file]


def has_nearby_symbol(schematic, row, start, end) -> bool:
    symbols = set([char for char in "".join(schematic) if char != "." and not char.isdigit()])
    width = len(schematic[0])  # All rows are uniform length
    if 1 <= row <= len(schematic) - 2:
        row_indices = [row-1, row, row+1]
    elif row == 0:
        row_indices = [0, 1]
    else:
        row_indices = [row-1, row]

    if 1 <= start and end <= width - 1:
        # regular
        column_indices = [i for i in range(start - 1, end + 2)]
    elif start == 0 and end <= width - 1:
        # cut off left
        column_indices = [i for i in range(0, end + 2)]
    elif 1 <= start and end == width - 1:
        # cut off right
        column_indices = [i for i in range(start - 1, end + 1)]
    else:
        # cut off both
        column_indices = [i for i in range(end + 1)]

    for row_index in row_indices:
        for column_index in column_indices:
            if schematic[row_index][column_index] in symbols:
                return True
    return False


def part1(data: list[str]) -> None:
    result = 0
    for idx, line in enumerate(data):
        start = 0
        end = 0
        is_iterating = False
        while True:
            if end > len(line) - 1 or start > len(line) - 1:
                break
            if not line[end].isdigit():
                if is_iterating:
                    is_iterating = False
                    if has_nearby_symbol(data, idx, start, end - 1):
                        print(idx, start, int(line[start:end]))
                        result += int(line[start:end])
                    start += end - start
                start += 1
                end += 1
            else:
                is_iterating = True
                end += 1
    print(result)


def part2(data: list[Any]) -> None:
    pass


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        puzzle = parse(f)
        part1(puzzle)
        part2(puzzle)
