def trebuchet(line):
    count = 0
    for char in line:
        if char.isnumeric():
            if count == 0:
                first = char
            last = char
            count += 1
    print(str(first), str(last))
    total = int(str(first) + str(last))
    # print('+', total)
    return total


def spelled_numbers(line):
    my_dict = {'one': -1, 'two': -1, 'three': -1, 'four': -1, 'five': -1, 'six': -1, 'seven': -1, 'eight': -1, 'nine': -1}
    if 'one' in line:
        my_dict['one'] = line.index('one')
    if 'two' in line:
        my_dict['two'] = line.index('two')
    if 'three' in line:
        my_dict['three'] = line.index('three')
    if 'four' in line:
        my_dict['four'] = line.index('four')
    if 'five' in line:
        my_dict['five'] = line.index('five')
    if 'six' in line:
        my_dict['six'] = line.index('six')
    if 'seven' in line:
        my_dict['seven'] = line.index('seven')
    if 'eight' in line:
        my_dict['eight'] = line.index('eight')
    if 'nine' in line:
        my_dict['nine'] = line.index('nine')
    # print(my_dict)

    # remove items that don't contain numbers in letters
    for k, v in list(my_dict.items()):
        if v == -1:
            del my_dict[k]
    # print(my_dict)

    sorted_list = sorted(my_dict, key=my_dict.get)
    # print(sorted_list)

    for x in sorted_list:
        if x == 'one':
            line = line.replace(x, '1')
        if x == 'two':
            line = line.replace(x, '2')
        if x == 'three':
            line = line.replace(x, '3')
        if x == 'four':
            line = line.replace(x, '4')
        if x == 'five':
            line = line.replace(x, '5')
        if x == 'six':
            line = line.replace(x, '6')
        if x == 'seven':
            line = line.replace(x, '7')
        if x == 'eight':
            line = line.replace(x, '8')
        if x == 'nine':
            line = line.replace(x, '9')
    # print(line)
    return line
