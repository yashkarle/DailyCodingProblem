# dutch national flag 3-way sorting algorithm
def str_encoding(ip_seq):
    low_r = 0
    mid_g = 0
    high_b = len(ip_seq) - 1

    while mid_g <= high_b:
        if ip_seq[mid_g] == 'R':
            # pull R out of the unknown space and shrink unknown space towards right
            ip_seq[low_r], ip_seq[mid_g] = ip_seq[mid_g], ip_seq[low_r]
            low_r += 1
            mid_g += 1
        elif ip_seq[mid_g] == 'G':
            # increment mid to accommodate G
            mid_g += 1
        else:
            # pull B out of the unknown space and shrink unknown space towards left
            ip_seq[mid_g], ip_seq[high_b] = ip_seq[high_b], ip_seq[mid_g]
            high_b -= 1

    return ip_seq


if __name__ == '__main__':
    input_seq = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

    result = str_encoding(input_seq)
    print(result)
