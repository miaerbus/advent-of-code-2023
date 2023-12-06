from lib import find_all


def cube_conundrum(line):
    game_number = int(line[line.index(' '): line.index(':')])

    for b in list(find_all(line, 'blue')):
        if int(line[int(b - 3): int(b - 1)]) > 14:
            return 0
    for g in list(find_all(line, 'green')):
        if int(line[int(g - 3): int(g - 1)]) > 13:
            return 0
    for r in list(find_all(line, 'red')):
        if int(line[int(r - 3): int(r - 1)]) > 12:
            return 0
    return game_number


def cube_conundrum_part_two(line):
    blue_max, green_max, red_max = 0, 0, 0
    for b in list(find_all(line, 'blue')):
        blue = int(line[int(b - 3): int(b - 1)])
        if blue > blue_max:
            blue_max = blue
    for g in list(find_all(line, 'green')):
        green = int(line[int(g - 3): int(g - 1)])
        if green > green_max:
            green_max = green
    for r in list(find_all(line, 'red')):
        red = int(line[int(r - 3): int(r - 1)])
        if red > red_max:
            red_max = red
    return blue_max * green_max * red_max
