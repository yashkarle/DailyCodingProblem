import statistics


def display_running_median(ip_sequence):
    stream = []
    for num in ip_sequence:
        stream.append(num)
        stream.sort()
        print(statistics.median(stream))


if __name__ == '__main__':
    input_sequence = [2, 1, 5, 7, 2, 0, 5]

    display_running_median(input_sequence)
