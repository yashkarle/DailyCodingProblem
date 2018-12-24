def min_classrooms(ip_list):
    classrooms = 0
    min_end = 999

    ip_list.sort(key=lambda tup: tup[0])

    for interval in ip_list:
        min_end = min(min_end, interval[1])
        if interval[0] < min_end:
            classrooms += 1

    return classrooms


if __name__ == '__main__':
    input_list = [(30, 75), (0, 50), (60, 150)]

    result = min_classrooms(input_list)
    print(result)
