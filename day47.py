def get_max_profit(ip_array):
    max_p = 0

    for i, num in enumerate(ip_array):
        for next_num in ip_array[i+1:]:
            if next_num - num > max_p:
                max_p = next_num - num

    return max_p


if __name__ == '__main__':
    input_array = [9, 11, 8, 5, 7, 10]
    max_profit = get_max_profit(input_array)
    print(max_profit)
