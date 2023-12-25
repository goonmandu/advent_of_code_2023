from typing import TextIO
import re


class Set:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"{self.red}R {self.green}G {self.blue}B"


class Game:
    def __init__(self, num: int, sets: list[Set] = None):
        self.num = num
        self.max_red = 0
        self.max_green = 0
        self.max_blue = 0
        if sets:
            self.max_red = max([s.red for s in sets])
            self.max_green = max([s.green for s in sets])
            self.max_blue = max([s.blue for s in sets])

    def add_games(self, sets: list[Set]):
        self.max_red = max([s.red for s in sets])
        self.max_green = max([s.green for s in sets])
        self.max_blue = max([s.blue for s in sets])

    def __str__(self):
        return f"#{self.num} {self.max_red}MaxR {self.max_green}MaxG {self.max_blue}MaxB"


def parse(file: TextIO) -> list[Game]:
    raw = [line.strip() for line in file]
    games = []
    for line in raw:
        gamenum_and_sets = re.split("; |: ", line)
        this_game = Game(int(gamenum_and_sets[0][5:]))
        sets = []
        for s in gamenum_and_sets[1:]:
            this_set = Set()
            sets_raw = re.split(", ", s)
            for color in sets_raw:
                if "red" in color:
                    this_set.red = int(color.replace(" red", ""))
                elif "green" in color:
                    this_set.green = int(color.replace(" green", ""))
                else:
                    this_set.blue = int(color.replace(" blue", ""))
            sets.append(this_set)
        this_game.add_games(sets)
        games.append(this_game)
    return games


def part1(data: list[Game]) -> None:
    th = (12, 13, 14)
    result = 0
    for game in data:
        if game.max_red <= th[0] \
                and game.max_green <= th[1] \
                and game.max_blue <= th[2]:
            result += game.num
    print(result)


def part2(data: list[Game]) -> None:
    result = 0
    for game in data:
        result += game.max_red * game.max_green * game.max_blue
    print(result)


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        puzzle = parse(f)
        part1(puzzle)
        part2(puzzle)
