import math


def printPowerSetO(set):
    set_size = len(set)
    power_set_size = (int)(math.pow(2, set_size))

    for counter in range(0, power_set_size):
        for j in range(0, set_size):
            if counter & (1 << j) > 0:
                print(set[j], end="")

        print("")


if __name__ == '__main__':
    ip_set = [1, 2, 3]
    printPowerSetO(ip_set)