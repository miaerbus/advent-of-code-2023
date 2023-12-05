from day1 import trebuchet, spelled_numbers

if __name__ == '__main__':
    file = open('day1-input', 'r')
    lines = file.readlines()
    total_sum = 0
    for line1 in lines:
        total_sum += trebuchet(spelled_numbers(line1))
    print('Sum:', total_sum)  # 54513
