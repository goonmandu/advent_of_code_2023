from typing import TextIO


def parse(file: TextIO) -> list[str]:
    return [line.strip() for line in file]


def part1(data: list[str]) -> None:
    result: int = 0
    for line in data:
        numbers: list[int] = [int(c) for c in line if c.isdigit()]
        result += numbers[0] * 10 + numbers[-1]
    print(result)


def part2(data: list[str]) -> None:
    digit_map: dict[str, int] = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    result: int = 0
    for line in data:
        numbers: list[int] = []
        start_scan: int = 0
        end_scan: int = 1
        while not (end_scan - 1 == len(line)):
            scanned = line[start_scan:end_scan]
            if scanned[-1].isdigit():
                numbers.append(int(scanned[-1]))
                start_scan += len(scanned)
            elif any(word in scanned for word in digit_map):
                for word in digit_map:
                    if word in scanned:
                        found: str = word
                        break
                numbers.append(digit_map[found])  # Safe to ignore name warning since elif assumes word in scanned
                start_scan += len(scanned) - 1
                end_scan -= 1
            end_scan += 1
        result += numbers[0] * 10 + numbers[-1]
    print(result)


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        puzzle = parse(f)
        part1(puzzle)
        part2(puzzle)
