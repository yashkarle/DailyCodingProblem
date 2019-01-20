import math


def print_power_set(set1):
    set_size = len(set1)
    power_set_size = int(math.pow(2, set_size))

    for counter in range(0, power_set_size):
        for j in range(0, set_size):
            if counter & (1 << j):
                print(set1[j], end="")

        print("")


if __name__ == '__main__':
    ip_set = [1, 2, 3]
    print_power_set(ip_set)
