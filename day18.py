def max_subarray(ip_list, k):
    op_list = []
    for i in range(0, len(ip_list) - k + 1):
        for j in range(i+1, k+i):
            for l in range(j+1, k+i):
                op_list.append(max(ip_list[i], ip_list[j], ip_list[k]))

    return op_list


if __name__ == '__main__':
    input_list = [10, 5, 2, 7, 8, 7]
    input_k = 3

    result = max_subarray(input_list, input_k)
    print(result)
