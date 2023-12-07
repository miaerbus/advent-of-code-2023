def wait_for_it(lines):
    times = []
    distances = []
    for char in lines[0].split():
        if char.isdigit():
            times.append(int(char))
    for char in lines[1].split():
        if char.isdigit():
            distances.append(int(char))

    total_count = []
    for i in range(len(times)):
        count = 0
        for j in range(times[i]):
            multiply = j*(times[i]-j)
            if multiply > distances[i]:
                count += 1
        total_count.append(count)

    total_multiply = 1
    for i in total_count:
        total_multiply *= i
    return total_multiply


def wait_for_it_part2(lines):
    times_char = ''
    distances_char = ''
    for char in lines[0].split():
        if char.isdigit():
            times_char += char
    for char in lines[1].split():
        if char.isdigit():
            distances_char += char
    times = int(times_char)
    distances = int(distances_char)

    count = 0
    for i in range(times):
        multiply = i*(times-i)
        if multiply > distances:
            count += 1
    return count


file = open('input', 'r')
lines = file.readlines()
print(wait_for_it(lines))  # 800280
print(wait_for_it_part2(lines))  # 45128024
